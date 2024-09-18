from flask import Flask, request, send_file
from datetime import datetime
import logging
import os
import requests

app = Flask(__name__)

# Set up logging (you can modify this to log to a file or database)
logging.basicConfig(level=logging.INFO)

def get_location(ip_address):
    """Fetch location data based on the IP address."""
    response = requests.get(f'https://ipinfo.io/{ip_address}/json')
    if response.status_code == 200:
        return response.json()
    return None

# Endpoint for serving the tracking pixel
@app.route('/pixel')
def tracking_pixel():
    """Serve the 1x1 tracking pixel and log the email open event."""
    # Extract query parameters from the request
    user_id = request.args.get('user_id')
    email_id = request.args.get('email_id')

    # Log the open event with timestamp, IP address, and user agent
    log_entry = {
        "user_id": user_id,
        "email_id": email_id,
        "opened_at": datetime.now().isoformat(),
        "ip_address": request.remote_addr,
        "user_agent": request.headers.get('User-Agent')
    }
    logging.info(f"Email opened: {log_entry}")

    # Get location data based on the IP address
    location_info = get_location(request.remote_addr)
    log_entry['location'] = location_info

    # Log the complete event details
    logging.info(f"Complete log entry: {log_entry}")

    # Serve a transparent 1x1 pixel image
    pixel_path = '/home/yourusername/yourapp/tracking_pixel.png'  # Absolute path to the image on PythonAnywhere
    if os.path.exists(pixel_path):
        return send_file(pixel_path, mimetype='image/png')
    else:
        logging.error("Pixel image not found.")
        return "Pixel image not found", 404

# Note: app.run() is not needed on PythonAnywhere since WSGI will handle running the app.
