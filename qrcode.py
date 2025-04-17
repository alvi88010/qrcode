import qrcode

data = input("Enter you data : ")

img = qrcode.make(data)
img.save("qrcode.png")
