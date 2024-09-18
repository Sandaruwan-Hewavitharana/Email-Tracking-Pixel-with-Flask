# Email Tracking Pixel with Flask

This project is a simple Flask web application that allows tracking when an email is opened by embedding a 1x1 transparent pixel into the email content. When the pixel is loaded, the app logs details such as the user ID, email ID, timestamp, IP address, and approximate location.

## Features
- Logs the following data when the tracking pixel is opened:
  - User ID and email ID from query parameters
  - Open time (timestamp)
  - IP address of the email recipient
  - User agent string of the recipient's email client
  - Location based on the IP address using the [ipinfo.io](https://ipinfo.io) service
  
## Prerequisites
- Python 3.7+
- Flask
- Internet connection to use [ipinfo.io](https://ipinfo.io) for location services

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your_username/email-tracking-pixel.git
   cd email-tracking-pixel
2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
4. Run the Flask application:

   ```bash
   python app.py
  The app will be running on http://127.0.0.1:5000/.
5. Embed the tracking pixel in your emails as follows:

   ```html
   <img src="http://your-domain.com/pixel?user_id=USER_ID&email_id=EMAIL_ID" width="1" height="1" style="display:none;" />

##Usage

1. To embed the tracking pixel in an email, insert an image tag like this:

   ```html
  
