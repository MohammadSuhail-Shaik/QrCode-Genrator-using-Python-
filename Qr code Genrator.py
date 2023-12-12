import qrcode
import datetime 

qr = qrcode.QRCode(version = 10, box_size = 4, border = 3)

input_data = input("Entre data: ")

qr.add_data(input_data)
qr.make(fit = True)

img = qr.make_image(fill = 'black', back_color = 'white')

date_time_format = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

img.save(f'qrcode{date_time_format}.png')
