from pyzbar.pyzbar import decode
from PIL import Image
decodeQr =decode (Image.open("qrcode.png"))
print(decodeQr[0].data.decode("ascii")) 