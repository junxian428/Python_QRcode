import qrcode

qr = qrcode.make('Hello World')
qr.save('myQR.png')