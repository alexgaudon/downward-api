#!/usr/bin/env python3
import os
import json
from flask import Flask, render_template, jsonify, url_for
from datetime import datetime

app = Flask(__name__, static_url_path='/static')

# Track application startup time
start_time = datetime.now()

def read_downward_api():
    """Read and display Downward API information."""
    # Get pod name from Downward API
    pod_name = os.getenv('POD_NAME', 'Not set')
    
    # Get pod namespace from Downward API
    pod_namespace = os.getenv('POD_NAMESPACE', 'Not set')
    
    # Get pod IP from Downward API
    pod_ip = os.getenv('POD_IP', 'Not set')
    
    # Get node name from Downward API
    node_name = os.getenv('NODE_NAME', 'Not set')
    
    # Get service account name from Downward API
    service_account = os.getenv('SERVICE_ACCOUNT', 'Not set')
    
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