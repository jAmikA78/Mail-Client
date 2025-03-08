import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# Mail settings
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_SENDER = "sender_mail@gmail.com"
EMAIL_PASSWORD = "**** **** **** ****"  # Consider using app password (read readme.md for more information)

recipients = [
    ["First_Name", "mail1@mail.com"],
    ["First_Name", "mail2@mail.com"],
    ["First_Name", "mail3@mail.com"],
    # Add more recipients here
]


def send_email():
    for recipient in recipients:
        # Create NEW message for each recipient
        msg = MIMEMultipart()
        msg["From"] = EMAIL_SENDER
        msg["To"] = recipient[1]  # recipient mail
        msg["Subject"] = "🎉 Congratulations! You're In - Welcome to Level 1 Phase 1 Training! "

        # Add logo attachment
        try:
            with open('logo/logo.png', 'rb') as img_file:
                logo = MIMEImage(img_file.read())
                logo.add_header('Content-ID', '<logo>')
                msg.attach(logo)
        except FileNotFoundError:
            print("⚠️ Warning: Logo file not found. Sending email without logo.")
        except Exception as e:
            print(f"⚠️ Error loading logo: {str(e)}")

        # Personalize content
        html_content = f"""
                <html>
                   <head>
                      <meta charset="utf-8">
                   </head>
                   <body style="font-family: Arial, sans-serif; line-height: 1.6; background-color: #f5f5f5; margin: 0; padding: 20px;">
                      <p>&nbsp;</p>
                      <!-- Logo Section -->
                      <div style="text-align: center; margin-bottom: 20px;">
                          <img src="cid:logo" alt="Company Logo" style="max-width: 200px; height: auto;">
                      </div>
                      <!-- Subject -->
                      <h1 style="color: #e74c3c; text-align: center; margin-bottom: 30px;"><span style="color: #c8272c;">MA</span><span style="color: #f4b316;">C</span><span style="color: #1dafec;">PC</span></h1>
                      <!-- Main Content -->
                      <div style="background-color: #f8f9fa; padding: 20px; border-radius: 8px; margin: 20px 0;">
                         <!-- recipient name -->
                         <strong>Dear {recipient[0]},</strong> 
                         <h2 style="color: #2c3e50; margin-top: 0;">🌟 Big News! 🌟</h2>
                         <p>We are thrilled to inform you that you've been selected for <strong style="color: #2980b9;">subject</strong>!</p>
                      </div>
                      <!-- WhatsApp Group Emphasis -->
                      <div style="background-color: #25d366; padding: 20px; border-radius: 8px; margin: 20px 0; text-align: center;">
                         <h3 style="color: white; margin: 0;">⚠️ Mandatory Join: WhatsApp Group</h3>
                         <p style="color: white; margin: 10px 0;"><a style="color: #fff; text-decoration: underline; font-weight: bold;" href="https://chat.whatsapp.com/groublink"> Click here to join our official group </a></p>
                      </div>
                      <!-- Website Link -->
                      <div style="text-align: center; margin: 25px 0;">
                         <p>Explore more about us on our website:<br /><a style="color: #3498db; text-decoration: none; font-weight: bold;" href="https://website_link"> sites.google.com/ma-icpc </a></p>
                      </div>
                      <!-- Footer -->
                      <div style="border-top: 2px solid #ecf0f1; padding-top: 20px; text-align: center;">
                         <p style="color: #7f8c8d;">Best regards,<br /><strong style="color: #2c3e50;">our Team</strong></p>
                         <p style="color: #7f8c8d; font-size: 0.9em;"your_mail@gmail.com <br />your organization</p>
                      </div>
                   </body>
                </html>
        """
        msg.attach(MIMEText(html_content, "html"))

        # Send individual emails
        try:
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()
                server.login(EMAIL_SENDER, EMAIL_PASSWORD)
                server.sendmail(EMAIL_SENDER, recipient, msg.as_string())
                print(f"✅ Email sent to {recipient}")
        except Exception as e:
            print(f"❌ Error sending to {recipient}: {str(e)}")


if __name__ == "__main__":
    send_email()
