import qrcode

# QR kod oluşturmak için bir metin veya bağlantı tanımlayın
link = "https://www.youtube.com"  # Burada kendi bağlantınızı kullanın

# QR kod oluşturma işlemi
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(link)
qr.make(fit=True)

# QR kodun görüntüsünü oluşturun
img = qr.make_image(fill_color="black", back_color="white")

# QR kodu bir dosyaya kaydedebilir veya görüntüleyebilirsiniz
img.save("qrcode.png")  # QR kodu qrcode.png adlı bir dosyaya kaydeder

# QR kodu görüntülemek için kullanabilirsiniz
img.show()
