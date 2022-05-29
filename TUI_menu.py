# create a TUI
import QR_VCARD
import QR_WHATSAPP

menu_screen = """
0. Quit
1. Create driver QR VCARD code from CSV
2. Create QR code for Whatsapp from CSV and manually assign driver

"""
while True:
    print(menu_screen)
    user_choice = input("Enter your choice: ")
    if user_choice == "0":
        print("Goodbye")
        break
    elif user_choice == "1":
        QR_VCARD.create_QR_VCARD()
    elif user_choice == "2":
        with open("data_booking_code.csv", "r") as booking_code:
            booking_code_list = booking_code.readlines()
        with open("data_drivers.csv", "r") as driver_name:
            driver_name_list = driver_name.readlines()
        #ignore t
        for booking in booking_code_list[1:]:
            #only print name and booking code
            print(booking.split(",")[1], booking.split(",")[0])  
            print( " please select a driver for this booking: ")
            for number, driver in enumerate(driver_name_list[1:] ,1 ):
                #print only driver name
                print(number, driver.split(",")[0])
            driver_choice = int(input("Enter number of driver: "))
            driver = driver_name_list[driver_choice]
            print("selected booking ", booking,
            "selected driver: ", driver)

            booking_code = booking.split(",")[0]
            name = booking.split(",")[1]
            cell_number = driver.split(",")[1]
            message = booking.split(",")[2]
            # print(booking_code,name,cell_number,message)
            QR_WHATSAPP.create_Whatsapp_QR(cell_number,
                        booking_code,
                        name,
                        message)
                        
                
            
                
            print("--------")
    
    else:
        print("Invalid choice")