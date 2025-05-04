#!/usr/bin/env python3
import os
import json
import time

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
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
    }
    
    return info

def main():
    """Main function to run the application."""
    print("Downward API Example")
    print("===================")
    
    while True:
        info = read_downward_api()
        print("\nCurrent Downward API Information:")
        print(json.dumps(info, indent=2))
        time.sleep(10)  # Update every 10 seconds

if __name__ == '__main__':
    main() 