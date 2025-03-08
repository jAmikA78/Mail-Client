# Bulk Email Sender with Personalized HTML Content

A Python script for sending personalized HTML emails with embedded images through Gmail's SMTP server. Designed for sending bulk emails while maintaining individual customization.

## Features

- 📨 Send personalized HTML emails to multiple recipients
- 🖼️ Embed logo/images in email content
- 💌 Gmail SMTP integration
- ✅ Error handling for failed deliveries
- 📝 HTML template with responsive design
- 🔒 TLS encryption for secure delivery

## Prerequisites

- Python 3.x
- Gmail account with [App Password](https://myaccount.google.com/apppasswords) enabled
- Basic understanding of HTML/CSS for template customization

## Configuration

1. **Email Credentials**  
   Replace in the script:
   ```python
   EMAIL_SENDER = "your.email@gmail.com"
   EMAIL_PASSWORD = "your-app-password"  # Never use your main password!
   ```

2. **Recipients List**  
   Update the recipients array:
   ```python
   recipients = [
       ["John Doe", "john@example.com"],
       ["Jane Smith", "jane@example.com"],
       # Add more recipients
   ]
   ```

3. **Logo Setup**  
   - Create a `logo` directory in your project folder
   - Add your logo as `logo.png` (or update the path in the script)

4. **Custom Content**  
   Update these sections in the HTML template:
   - WhatsApp group link
   - Website URL
   - Organization name
   - Footer information

## Usage

1. **Test Configuration**  
   Run with a single test recipient:
   ```bash
   python email_sender.py
   ```

2. **Successful Send**  
   You'll see confirmation messages:
   ```
   ✅ Email sent to ['John Doe', 'john@example.com']
   ```

3. **Error Handling**  
   The script will show errors for failed attempts:
   ```
   ❌ Error sending to ['Invalid', 'invalid@mail']: (error details)
   ```

## Security Best Practices

- 🔑 Always use an App Password instead of your main Google account password
- 🛡️ Never commit sensitive data to version control
- 🚨 Consider using environment variables for credentials:
  ```python
  EMAIL_SENDER = os.environ.get('GMAIL_USER')
  EMAIL_PASSWORD = os.environ.get('GMAIL_APP_PASS')
  ```

## Customization Guide

1. **Email Template**  
   Modify the HTML content in the `html_content` variable:
   - Change colors (hex codes)
   - Modify layout structure
   - Add/remove sections
   - Update branding elements

2. **Attachments**  
   To add more attachments:
   ```python
   # Add after logo attachment
   with open('file.pdf', 'rb') as f:
       pdf = MIMEApplication(f.read())
       pdf.add_header('Content-Disposition', 'attachment', filename='document.pdf')
       msg.attach(pdf)
   ```

3. **SMTP Configuration**  
   For other email providers:
   ```python
   SMTP_SERVER = "smtp.provider.com"  # e.g., "smtp.outlook.com"
   SMTP_PORT = 587                    # Typically 465 for SSL
   ```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Authentication Errors | Verify App Password & 2FA setup |
| Missing Logo Warning | Check path/name in `logo/logo.png` |
| Connection Refused | Allow less secure apps (temporarily) |
| HTML Rendering Issues | Validate HTML structure & CSS |
| Slow Sending | Add delay between emails (1-2s) |

## Disclaimer

- Use this script responsibly and in compliance with [CAN-SPAM Act](https://www.ftc.gov/tips-advice/business-center/guidance/can-spam-act-compliance-guide-business)
- Test with small batches before full deployment
- Maintain proper unsubscribe mechanisms for bulk emails