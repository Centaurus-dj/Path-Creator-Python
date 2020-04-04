# -*- coding: utf-8 -*-
import subprocess
import os
import pathlib
import tkinter
import time
from tkinter import *
from pathlib import Path

##Functions
def myfunc(Event):
    nbre_choisi = str(directoryent.get())
    directoryent.delete(0, END)
    if not nbre_choisi:
        text1["text"] = "You didn't entered a name"
        time.sleep(1)
    elif nbre_choisi == nbre_choisi:
        text1["text"] = "You entered a name"
        time.sleep(1)
        ##Input of informations needed
        directory = str(nbre_choisi)
        parent_dir = Path("C:/pythonscript_test/Folders_Created/")
        myPath = parent_dir / directory
        ##We create a condition to be sure te folder is created
        if not os.path.exists(myPath):
            os.makedirs(myPath)
            ##We inform the user of the creation of the folder
            text2["text"] = "Directory '% s' well created"  % myPath
            time.sleep(1)
            ##Variable Construction
            commandeOuverture = "explorer " + str(myPath)
            text3["text"] = "We are opening the folder..."
            time.sleep(1)
            ##We open the folder using Popen
            subprocess.Popen(commandeOuverture, shell=True)

        elif os.path.exists(myPath):
            ##We inform the user that the folder in question already exists
            text2["text"] = "Directory '% s' already exists" % myPath
            time.sleep(1)
            ##Variable Construction
            commandeOuverture = "explorer " + str(myPath)
            text3["text"] = "We are opening the folder..."
            time.sleep(1)
            ##We open the folder using Popen
            subprocess.Popen(commandeOuverture, shell=True)
        else:
            pass

    










##Creating window with Tkinter module
window = Tk()

##We set the background color in hexadecimal
window.configure(background='#323232')

##We set the width and the height of the window
window.configure(width="600", height="400")

##Title of the Window
title = Label(window, text="Path creator", font=("", 23), background="#323232", fg="#ffffff")
title.grid(row=0, column=1, pady=12, padx=300)

##Labels
lbl_reponse = Label(window, text="Choose a name for your folder", font=("", 15), background="#323232", fg="#ffffff")
lbl_reponse.grid(row=1, column=1, pady=5, padx=5)
text1 = Label(window, text="", font=("", 15), background="#323232", fg="#ffffff")
text1.grid(row=3, column=1, pady=5, padx=5)
text2 = Label(window, text="", font=("", 15), background="#323232", fg="#ffffff")
text2.grid(row=4, column=1, pady=5, padx=5)
text3 = Label(window, text="", font=("", 15), background="#323232", fg="#ffffff")
text3.grid(row=5, column=1, pady=5, padx=5)

##Input as Entries
directoryent = Entry(window, background="#323232", fg="#ffffff", font=("", 23))
directoryent.grid(row=2, column=1, pady=5, padx=5)
directoryent.bind("<Return>", myfunc)


##Start the app
window.mainloop()
