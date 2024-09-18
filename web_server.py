from flask import Flask, request, send_file
from datetime import datetime
import logging
import os
import requests

app = Flask(__name__)

# Set up logging (you can modify this to log to a file or database)
logging.basicConfig(level=logging.INFO)

def get_location(ip_address):
    response = requests.get(f'https://ipinfo.io/{ip_address}/json')
    if response.status_code == 200:
        return response.json()
    return None

# Endpoint for serving the tracking pixel
@app.route('/pixel')
def tracking_pixel():
    # Extract query parameters from the request
    user_id = request.args.get('user_id')
    email_id = request.args.get('email_id')
    
    # Log the open event with timestamp and IP address
    log_entry = {
        "user_id": user_id,
        "email_id": email_id,
        "opened_at": datetime.now().isoformat(),
        "ip_address": request.remote_addr,
        "user_agent": request.headers.get('User-Agent')
    }
    logging.info(f"Email opened: {log_entry}")

    # Get location data from IP address
    location_info = get_location(request.remote_addr)
    log_entry['location'] = location_info
    
    logging.info(f"Email opened: {log_entry}")
    
    # Serve a transparent 1x1 pixel image
    pixel_path = 'tracking_pixel.png'  # You can generate or store a transparent pixel image
    return send_file(pixel_path, mimetype='image/png')

if __name__ == '__main__':
    # Ensure the pixel image exists at the specified path
    if not os.path.exists('tracking_pixel.png'):
        raise FileNotFoundError("tracking_pixel.png image not found.")
    app.run(host='0.0.0.0', port=5000)
