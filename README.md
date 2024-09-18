# Flask Email Tracking Pixel

A lightweight Flask application to track email opens using an embedded tracking pixel. This project logs the user's IP address, the time the email was opened, and the user's approximate location using an external IP geolocation service.

## Features

- Track email opens with a 1x1 invisible pixel.
- Log details such as:
  - User's IP address.
  - Email open timestamp.
  - User agent (browser, email client).
  - Approximate location using IP geolocation.
- Use a simple backend based on Flask and Python.
  
## Getting Started

### Prerequisites

Ensure you have Python installed on your machine. This application uses Python 3.6+ and requires `Flask` and `requests` for basic functionality.

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/flask-email-tracking-pixel.git
    cd flask-email-tracking-pixel
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Generate the transparent 1x1 pixel image (or provide your own):

    ```python
    from PIL import Image

    img = Image.new('RGBA', (1, 1), (255, 255, 255, 0))
    img.save('tracking_pixel.png')
    ```

4. Run the Flask application:

    ```bash
    python app.py
    ```

5. Access the application at `http://127.0.0.1:5000/pixel?user_id=123&email_id=abc`.

### How It Works

When you send an email with an HTML image tag that points to this Flask app's `/pixel` endpoint, the user's email client will request the image. This will trigger the Flask application to log the following information:

- **User ID**: Passed via URL query parameters.
- **Email ID**: Passed via URL query parameters.
- **Opened Time**: Logged as the exact time the email was opened.
- **IP Address**: The user's IP address is logged.
- **Location**: The application fetches approximate geographic data based on the user's IP address using the `ipinfo.io` API.

### Example HTML for Embedding the Tracking Pixel

```html
<img src="http://your-domain.com/pixel?user_id=12345&email_id=abcdef" width="1" height="1" style="display:none;">
