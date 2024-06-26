from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES

from tkinter import *
from tkinter import messagebox

import os

# directory = os.path.dirname(__file__)
directory = 'D:/_programming/EncryptionTool/files'


passwordFile = '/_safe/password.txt'
passwordDir = directory + passwordFile
salt = get_random_bytes(32)
with open(passwordDir, 'rb') as p:
    password = p.read()

keyFile = '/_safe/key.bin'
keyDir = directory + keyFile
key = PBKDF2(password, salt, dkLen=32)
with open(keyDir, 'wb') as k:
    k.write(key)

window = Tk()
window.wm_withdraw()
messagebox.showinfo("Key Generated Successfully", "The key file has been generated")
