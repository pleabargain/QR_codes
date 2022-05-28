# requirements
# pip install pillow
# pip install qrcode


# This code will read in a CSV or XLS file 

# reference information
# https://en.wikipedia.org/wiki/VCard
# vcard v4 output the file contains

# BEGIN	All vCards must start with this property.	BEGIN:VCARD
# VERSION	Required	The version of the vCard specification. In version 4.0, this must come right after the BEGIN property.	VERSION:3.0
# FN	Required	The formatted name string associated with the vCard object.	FN:Dr. John Doe
# TEL	Optional	The canonical number string for a telephone number for telephony communication with the vCard object.	TEL;TYPE=cell:(123) 555-5832
# LANG		Optional	Defines a language that the person speaks.	LANG:fr-CA
# PHOTO	Optional	Optional	Optional	An image or photograph of the individual associated with the vCard. It may point to an external URL or may be embedded in the vCard as a Base64 encoded block of text.	2.1: PHOTO;JPEG:http://example.com/photo.jpg
    # 4.0: PHOTO;MEDIATYPE=image/jpeg:http://example.com/photo.jpg
    # 4.0: PHOTO:data:image/jpeg;base64,[base64-data]
# ORG		Optional	The name and optionally the unit(s) of the organization associated with the vCard object. This property is based on the X.520 Organization Name attribute and the X.520 Organization Unit attribute.	ORG:Google;GMail Team;Spam Detection Squad
# URL		Optional	A URL pointing to a website that represents the person in some way.	URL:http://www.johndoe.com
# END		Required	All vCards must end with this property.	END:VCARD


import csv
import pillow
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