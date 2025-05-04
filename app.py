#!/usr/bin/env python3
import os
import json
from flask import Flask, render_template, jsonify
from datetime import datetime

app = Flask(__name__)

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
    """Render the main page."""
    return render_template('index.html')

@app.route('/api/info')
def get_info():
    """API endpoint to get Downward API information."""
    return jsonify(read_downward_api())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080) 