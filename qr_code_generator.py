# from
# https://medium.com/towards-data-science/generate-qrcode-with-python-in-5-lines-42eda283f325

# requirements
# pip install pillow
# pip install qrcode


import qrcode
# Link for website
input_data = "https://towardsdatascience.com/face-detection-in-10-lines-for-beginners-1787aa1d9127"
#Creating an instance of qrcode
qr = qrcode.QRCode(
        version=3,
        box_size=10,
        border=5)
qr.add_data(input_data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save('qrcode001.png')