# from
# https://medium.com/towards-data-science/generate-qrcode-with-python-in-5-lines-42eda283f325

# requirements
# pip install pillow
# pip install qrcode


# This code will read in a CSV or XLS file 

# reference information
# https://en.wikipedia.org/wiki/VCard
# vcard v4 output the file contains

# BEGIN	All vCards must start with this property.	BEGIN:VCARD
# VERSION	Required	The version of the vCard specification. In version 4.0, this must come right after the BEGIN property.	
# FN	Required	The formatted name string associated with the vCard object.	FN:Dr. John Doe
# TEL	Optional	The canonical number string for a telephone number for telephony communication with the vCard object.	TEL;TYPE=cell:(123) 555-5832
# LANG		Optional	Defines a language that the person speaks.	LANG:fr-CA
# PHOTO	Optional	Optional	Optional	An image or photograph of the individual associated with the vCard. It may point to an external URL or may be embedded in the vCard as a Base64 encoded block of text.	2.1: PHOTO;JPEG:http://example.com/photo.jpg
    # 4.0: PHOTO;MEDIATYPE=image/jpeg:http://example.com/photo.jpg
    # 4.0: PHOTO:data:image/jpeg;base64,[base64-data]
# ORG		Optional	The name and optionally the unit(s) of the organization associated with the vCard object. This property is based on the X.520 Organization Name attribute and the X.520 Organization Unit attribute.	ORG:Google;GMail Team;Spam Detection Squad
# URL		Optional	A URL pointing to a website that represents the person in some way.	URL:http://www.johndoe.com
# END		Required	All vCards must end with this property.	END:VCARD

###
# read a csv with phone number and booking code.
# include booking code in the message in Whatsapp
# sample message:  https://wa.me/1XXXXXXXXXX?text=I'm%20interested%20in%20your%20car%20for%20sale


#  https://wa.me/{"TYPE=CELL:"}?text={BOOKING_CODE}{MESSAGE}



# import csv
# import pillow
import qrcode
import time
from urllib.parse import quote


# create a function that returns current time in minutes and seconds
# move to tools lib in the future
def get_current_time():
    return time.strftime("%H_%M_%S")


def create_Whatsapp_QR(cell_number="971568753642",
                        booking_code="6t7y8u",
                        name=None,
                        message="Please contact me ASAP"):
    # create a QR code for Whatsapp
    # https://wa.me/{cell_number}?text={BOOKING_CODE}{MESSAGE}
    # message += " My booking code is: " + booking_code
    
    if name is None:
        name = ""
    else:
        message += "My name is: " + name + ".\n"
        message += "My booking code is: " + booking_code
    # print(message)
    message = quote(message)
    # print(message)
    

    result = f"https://wa.me/{cell_number}?text={message}"
    print(result)
    qr = qrcode.QRCode(
                    version=4,
                    box_size=10,
                    border=5)
    qr.add_data(result)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    # give the name of the image from first cell in CSV
    img.save(get_current_time() + "_" + booking_code +'_whatsapp_qrcode' + '.png')
    print("Whatsapp QR code image generated")









if __name__ == "__main__":
    create_Whatsapp_QR(name ="Dennis")

