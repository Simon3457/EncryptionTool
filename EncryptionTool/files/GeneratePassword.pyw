from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

import string
import secrets
import random
import os

def main():

    window = Tk()
    window.title("Password Generator")
    window.wm_withdraw()
    
    # directory = os.path.dirname(__file__)
    directory = 'D:/_programming/EncryptionTool/files'
    passwordFile = '/_safe/password.txt'
    passwordDir = directory + passwordFile
    
    length = simpledialog.askinteger("Input Length", "What is the desired length of your password?",
                                     parent=window, minvalue=0, maxvalue=10000)
    password = ""

    if length is not None:
        for i in range(length):
            randInt = random.randint(1, 3)
            if(randInt == 1):
                password += secrets.choice(string.ascii_letters)
            elif(randInt == 2):
                password += secrets.choice(string.digits)
            elif(randInt == 3):
                password += secrets.choice(string.punctuation)

        pw = bytes(password, 'utf-8')
        with open(passwordDir, 'wb') as p:
            p.write(pw)

        messagebox.showinfo("Password Generator", "Password generated successfully")

    else:
        messagebox.showerror("Password Generator", "Operation cancelled")
    

main()
