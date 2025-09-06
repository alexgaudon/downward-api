#!/usr/bin/env python3
import os
import json
from flask import Flask, render_template, jsonify, url_for, send_from_directory
from datetime import datetime
import time
import random


app = Flask(__name__, static_url_path='/static')

# Track application startup time
start_time = datetime.now()

# Set cache timeout for static files (1 hour in seconds)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 3600

def read_downward_api():
    """Read and display Downward API information."""
    # Get pod name from Downward API
    pod_name = os.getenv('POD_NAME')

    # Get pod namespace from Downward API
    pod_namespace = os.getenv('POD_NAMESPACE')

    # Get pod IP from Downward API
    pod_ip = os.getenv('POD_IP')

    # Get node name from Downward API
    node_name = os.getenv('NODE_NAME')

    # Get service account name from Downward API
    service_account = os.getenv('SERVICE_ACCOUNT')

    # Mock values for local development
    if not pod_name:
        pod_name = 'downward-api-example-pod'
    if not pod_namespace:
        pod_namespace = 'development'
    if not pod_ip:
        pod_ip = '192.168.1.100'
    if not node_name:
        node_name = f'k8s-worker-{random.randint(1, 3)}'
    if not service_account:
        service_account = 'development'

    # Create a dictionary with all the information
    info = {
        'pod_name': pod_name,
        'pod_namespace': pod_namespace,
        'pod_ip': pod_ip,
        'node_name': node_name,
        'service_account': service_account,
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

    return info

@app.route('/')
def index():
    """Render the main page with server-side data."""
    info = read_downward_api()
    return render_template('index.html', info=info)

@app.route('/api/info')
def get_info():
    """API endpoint to get Downward API information."""
    return jsonify(read_downward_api())

@app.route('/static/<path:filename>')
def custom_static(filename):
    """Serve static files with proper cache headers."""
    response = send_from_directory('static', filename)
    # Add cache control headers
    if filename.startswith('images/'):
        # Set longer cache time for images (1 day in seconds)
        response.headers['Cache-Control'] = 'public, max-age=86400'
    else:
        # Standard cache time for other static files
        response.headers['Cache-Control'] = 'public, max-age=3600'
    return response

@app.route('/health')
def health():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'uptime': str(datetime.now() - start_time)
    }), 200

@app.route('/ready')
def ready():
    """Readiness probe endpoint."""
    # Add any readiness checks here
    # For example, check if the application can access required resources
    try:
        # Basic check: can we read environment variables?
        _ = read_downward_api()
        return jsonify({
            'status': 'ready',
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }), 200
    except Exception as e:
        return jsonify({
            'status': 'not ready',
            'error': str(e)
        }), 503

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080) 