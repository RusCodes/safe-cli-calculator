import qrcode

img = qrcode.make("https://youtu.be/QkCa--fyGjA?si=uL2TyOJaM_hNVBWZ")
img.save("qr2.png", "PNG")