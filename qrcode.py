import pyqrcode
url = pyqrcode.create(input())
url.svg('uca-url . svg', scale = 8)
print(url.terminal(quiet_zone=1))
