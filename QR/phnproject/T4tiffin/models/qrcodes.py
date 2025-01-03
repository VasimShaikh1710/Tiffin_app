from django.db import models
from .students import StudentRegistration
import qrcode
from io import BytesIO
import base64
from PIL import Image
import os
from django.conf import settings

class Qrcodes(models.Model):
    username = models.ForeignKey(StudentRegistration, on_delete=models.CASCADE)
    parmanantqr_base64 = models.TextField(blank=True)  # Base64 encoded QR code
    multiple_base64 = models.TextField(blank=True)  # Base64 encoded QR code
    encrypt1 = models.CharField(max_length=500)
    encrypt2 = models.CharField(max_length=500)

    def save(self, *args, **kwargs):
        # Helper function to generate QR code with logo and return base64
        def generate_qr_with_logo(data, logo_relative_path):
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction for logo
                box_size=10,
                border=4,
            )
            qr.add_data(data)
            qr.make(fit=True)

            # Create the QR code image
            qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

            # Resolve full path for logo in static files
            logo_path = os.path.join(settings.BASE_DIR, "T4tiffin", "static", logo_relative_path)

            # Open logo
            try:
                logo = Image.open(logo_path)
                print("Logo loaded successfully.")
            except Exception as e:
                print(f"Error loading logo: {e}")
                return None

            # Resize logo to fit within the QR code
            qr_width, qr_height = qr_img.size
            logo_size = int(qr_width * 0.8)  # Adjust logo size
            logo = logo.resize((logo_size, logo_size))

            # Calculate position for the logo
            pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)

            # Paste logo onto QR code
            qr_img.paste(logo, pos, mask=logo)

            # Convert to Base64
            buffer = BytesIO()
            qr_img.save(buffer, format="PNG")
            buffer.seek(0)
            qr_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

            return qr_base64

        # Path relative to the static folder
        logo_relative_path = "images/qrlogo.png"

        # Generate QR codes and store them as base64
        if not self.parmanantqr_base64:
            self.parmanantqr_base64 = generate_qr_with_logo(self.encrypt1, logo_relative_path)

        if not self.multiple_base64:
            self.multiple_base64 = generate_qr_with_logo(self.encrypt2, logo_relative_path)

        super().save(*args, **kwargs)
