from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

import base64
import os
import sys


def decryption():
    # Get password from text box and compare it with the password.txt file to replicate authentication
    password = code.get()
    passwordFile = '/files/_safe/password.txt'
    passwordDir = directory + passwordFile
    with open(passwordDir, 'rb') as p:
        data = p.read()
    db_pw = data.decode()

    # If password is correct & filename is not null, attempt to open the file
    if password == db_pw:
        filename = filedialog.askopenfilename()

        if filename != "":
            # Open file to decrypt
            with open(filename, 'rb') as e:
                iv = e.read(16)
                decrypt_data = e.read()

            # Access secret key
            keyFile = '/files/_safe/key.bin'
            keyDir = directory + keyFile
            with open(keyDir, 'rb') as k:
                key = k.read()

            # Create cipher, decode/unpad & write to decrypted.txt 
            decryptedFile = '/files/_safe/decrypted.txt'
            decryptedDir = directory + decryptedFile
            cipher = AES.new(key, AES.MODE_CBC, iv=iv)
            decode_message = unpad(cipher.decrypt(decrypt_data), AES.block_size)
            with open(decryptedDir, 'wb') as d:
                d.write(decode_message)

            messagebox.showinfo("Decryption Successful", "The text file has been decrypted in the decrypted.txt file")

        # If no file has been chosen or user hit cancel, show warning box
        else:
            messagebox.showerror("Encryption", "Operation cancelled")
            
    # If password input is null, show warning to input password
    elif password == "":
        messagebox.showwarning("Decryption", "Please Input Password")

    # If password input does not match text file password, show error
    elif password != db_pw:
        messagebox.showerror("Decryption", "Invalid Password")
        


def encryption():
    # Get password from text box and compare it with the password.txt file to replicate authentication
    password = code.get()
    passwordFile = '/files/_safe/password.txt'
    passwordDir = directory + passwordFile
    with open(passwordDir, 'rb') as p:
        data = p.read()
    db_pw = data.decode()

    # If password is correct & filename is not null, attempt to open the file
    if password == db_pw: 
        filename = filedialog.askopenfilename()

        if filename != "":
            # Open file to encrypt
            with open(filename, 'rb') as s:
                message = s.read()
            
            # Access secret key
            keyFile = '/files/_safe/key.bin'
            keyDir = directory + keyFile
            with open(keyDir, 'rb') as k:
                key = k.read()

            # Create cipher, decode/unpad & write to encrypted.bin 
            cipher = AES.new(key, AES.MODE_CBC)
            cipher_data = cipher.encrypt(pad(message, AES.block_size))
            encryptedFile = '/files/_safe/encrypted.bin'
            encryptedDir = directory + encryptedFile
            with open(encryptedDir,'wb') as e:
                e.write(cipher.iv)
                e.write(cipher_data)
            
            messagebox.showinfo("Encryption Successful", "The file has been encrypted in the encrypted.bin file")

        # If no file has been chosen or user hit cancel, show warning box
        else:
            messagebox.showerror("Encryption", "Operation cancelled")

    # If password input is null, show warning to input password
    elif password == "":
        messagebox.showwarning("Encryption", "Please Input Password")

    # If password input does not match database password, show error
    elif password != db_pw:
        messagebox.showerror("Encryption", "Invalid Password")
        


def main_window():
    global window
    global code
    global filename
    global key
    global message
    global directory
    
    # Create GUI window for program based off Tkinter library
    window = Tk()
    window.geometry("406x260")
    window.configure(bg = "#AA99FF")
    window.title("File Encryption Tool (AES-256)")

    # Get directory path, then grab image icon for app from relative path
    # directory = os.path.dirname(__file__)
    directory = 'D:/_programming/EncryptionTool'
    iconFile = '/files/_safe/key_icon.png'
    iconDir = directory + iconFile
    icon = PhotoImage(file = iconDir)
    window.iconphoto(False, icon)

    # Encryption button (takes in any type of file) & Decryption button (takes in a binary (.bin) file
    Label(text="Select file to encrypt", fg="black", bg="#AA99FF", font=("calibri",14)).place(x=10,y=10)
    Button(text="ENCRYPT", height="5", width=26, bg="green", fg="white", bd=0, command=encryption).place(x=10, y=40)
    Label(text="Select bin file to decrypt", fg="black", bg="#AA99FF", font=("calibri",14)).place(x=208,y=10)
    Button(text="DECRYPT", height="5", width=26, bg="blue", fg="white", bd=0, command=decryption).place(x=208, y=40)

    # Password input text box (must match password in the files/password.txt file)
    Label(text="Enter secret key: ", fg="black", bg="#AA99FF", font=("calibri",14)).place(x=10,y=130)
    code = StringVar()
    Entry(textvariable=code, width=19, bd=0, font=('arial',25), show="*").place(x=10, y=160, width=386)

    # Button with function to clear password text box
    def reset():
        code.set("")
    Button(text="RESET", height="2", width=54, bg="red", fg="white", bd=0, command=reset).place(x=11, y=210)

    window.mainloop()

main_window()
