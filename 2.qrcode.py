import qrcode
from PIL import Image

# Create a QRCode instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

# Add data to the QR code
qr.add_data("Hey! My Name is Mahendra")
qr.make(fit=True)

# Generate the QR code image
img = qr.make_image(fill_color="red", back_color="blue")

# Save the QR code image
img.save("your_qrcode.png")
