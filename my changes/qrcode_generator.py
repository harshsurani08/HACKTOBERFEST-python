# Import QRCode from pyqrcode
import pyqrcode
from pyqrcode import QRCode
  
  
# String which represents the QR code
inp = input("Enter Text you want QR code of: ")
  
# Generate QR code
url = pyqrcode.create(inp)
  
# Create and save the svg file naming "{user input}.svg"
url.svg(f"{inp}.svg", scale = 8)