#import pyqrcode
#import png 
#from PIL import Image
#link = input("patreon.com/thefightcoach")
#qr_code = pyqrcode.create(link)
#qr_code.png("TheFightCoach.png", scale=20)


# Import QRCode from pyqrcode 
import pyqrcode 
from pyqrcode import QRCode 
  
# URL string
site = "patreon.com/thefightcoach"
  
# Generate QR code 
getqrcode = pyqrcode.create(site) 
  
# save in svg file format
getqrcode.png("thefightcoach.png", scale = 10) 
