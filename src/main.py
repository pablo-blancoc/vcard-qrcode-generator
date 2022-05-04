import qrcode
import os

# write all information
name = ""
last_name = ""
title = ""
organization = ""
url = ""
cellphone = ""
fill_color = "#002642"
back_color = "white"

# create information string
qrcode_info = f"""
BEGIN:VCARD
VERSION:3.0
N:{last_name}; {name}
FN:{name} {last_name}
TITLE:{title}
ORG:{organization}
URL:{url}
TEL;TYPE=voice,cell,pref:{cellphone}
END:VCARD
"""

# create qrcode instance
qrcode = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

# add data to the instance and render it
qrcode.add_data(qrcode_info)
qrcode.make(fit=True)

# create the image and save it
img = qrcode.make_image(fill_color=fill_color, back_color=back_color)
img.save(os.path.join("files", f"{name}{last_name}.png"))
