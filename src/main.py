import os
import qrcode
from PIL import Image

PATH = os.getcwd()
LOGO_NAME = ""
NAME = ""
LAST_NAME = ""
TITLE = ""
ORGANIZATION = ""
URL = ""
CELLPHONE = ""
WORKPHONE = ""
EMAIL = ""
FILL_COLOR = ""
BACK_COLOR = ""

# create information string
qrcode_info = f"""
BEGIN:VCARD
VERSION:3.0
N:{LAST_NAME};{NAME};;;
FN:{NAME} {LAST_NAME}
TITLE:{TITLE}
ORG:{ORGANIZATION}
URL:{URL}
TEL;TYPE=voice,cell,pref:{CELLPHONE}
TEL;TYPE=voice,work:{WORKPHONE}
EMAIL;TYPE=internet,pref:{EMAIL}
END:VCARD
""".strip()

# create qrcode instance
qrcode = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=2,
)

# add data to the instance and render it
qrcode.add_data(qrcode_info)
qrcode.make(fit=True)

# create the image and save it
img = qrcode.make_image(fill_color=FILL_COLOR, back_color=BACK_COLOR)

# add logo
logo = Image.open(os.path.join(PATH, "files", LOGO_NAME))
__basewidth = 200
__wpercent = __basewidth / float(logo.size[0])
__hsize = int((float(logo.size[1]) * float(__wpercent)))
logo = logo.resize((__basewidth, __hsize), Image.Resampling.LANCZOS)

pos = (
    (img.size[0] - logo.size[0]) // 2,
    (img.size[1] - logo.size[1]) // 2,
)
img.paste(logo, pos)

# save image
img.save(os.path.join(PATH, "files", f"{NAME}{LAST_NAME}.png"))
