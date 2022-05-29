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


import csv
# import pillow
import qrcode
import time


# create a function that returns current time in minutes and seconds
def get_current_time():
    return time.strftime("%H_%M_%S")


def create_QR_VCARD(source_csv='QR_code_sample_data.csv'):
# open a csv for reading as UTF-8   (with the encoding parameter)
    with open (source_csv, encoding='utf-8') as csvfile:

        # creating a csv reader object 
        csvreader = csv.reader(csvfile) 
    # extracting field names through first row 
        fields = next(csvreader) 
    # extracting each data row one by one 
        for row in csvreader: 
            # printing each row
            print(row)
            # print first cell in row 0
            print(row[0])
            input_data = "BEGIN:VCARD\n"
            input_data += "VERSION:4.0\n"
            input_data += "FN:" + row[0] + "\n"
            input_data += "TYPE=CELL:" + row[1] + "\n"
            input_data += "TEL;TYPE=WORK:" + row[2] + "\n"
            input_data += "URL:" + row[3] + "\n"
            input_data += "LANG:" + row[4] + "\n"
            input_data += "TITLE:" + row[5] + "\n"
            input_data += "ORG:" + row[6] + "\n"
            input_data += "END:VCARD" + "\n"
            # save the input_data to a separte file  using the name of the first cell in row 0
            # file extension .vcard
            with open ('aCSV_qrcode' + row[0] + ".vcard", "w") as f:
                f.write(input_data)

            
            #Creating an instance of qrcode version 4.0
            qr = qrcode.QRCode(
                    version=4,
                    box_size=10,
                    border=5)
            qr.add_data(input_data)
            qr.make(fit=True)
            img = qr.make_image(fill='black', back_color='white')
            # give the name of the image from first cell in CSV
            img.save(get_current_time()+'_CSV_qrcode' + row[0] + '.png')
        print("QR VCARD image generated")
            
if __name__ == "__main__":
    create_QR_VCARD()

