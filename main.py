# -*- coding: utf-8 -*-
import subprocess
import os
import pathlib
import tkinter
import time
from pathlib import Path


##Functions
##When called it creates the folder(s) asked by user and open an file explorer window in the folder
def myfunc(Event):
    nbre_choisi = str(directoryent.get())
    directoryent.delete(0, END)
    if not nbre_choisi:
        text1.grid(row=8, column=1, pady=5, padx=5)
        time.sleep(1)
    else:
        ##Input of informations needed
        directory = str(nbre_choisi)
        str_comp_usr = str(comp_usr.get())
        str_comp_drive = str(comp_drive.get())
        str_env = str(env.get())
        str_sys = str(sys.get())
        if str_sys == "Windows":
            parent_dir = Path(str_comp_drive+":/Users/"+str_comp_usr+"/"+str_env)
            myPath = parent_dir / directory
        elif str_sys == "Linux":
            parent_dir = Path("/home/"+str_comp_usr+"/"+str_env)
            myPath = parent_dir / directory
        ##We create a condition to be sure te folder is created
        if not os.path.exists(myPath):
            os.makedirs(myPath)
            ##Variable Construction
            commandeOuverture = "explorer " + str(myPath)
            text2.grid(row=9, column=1, pady=5, padx=5)
            time.sleep(1)
            ##We open the folder using Popen
            subprocess.Popen(commandeOuverture, shell=True)
        elif os.path.exists(myPath):
            ##Variable Construction
            commandeOuverture = "explorer " + str(myPath)
            text2.grid(row=9, column=1, pady=5, padx=5)
            time.sleep(1)
            ##We open the folder using Popen
            subprocess.Popen(commandeOuverture, shell=True)
        else:
            pass

##When called it informs the User of the drive selected
def print_selection():
    l2.grid_forget()
    l3.grid_forget()
    l4.grid_forget()
    l.grid(row=12, column=0, padx=5)


##When called it informs the User of the start folders selected
def print_selection2():
    l.grid_forget()
    l3.grid_forget()
    l4.grid_forget()
    l5.grid_forget()
    l2.grid(row=12, column=0, padx=5)

##When called it translates all the text in French
def translate_Fr():
    title.configure(text="Créateur de répertoire")
    lbl_sys.configure(text="Quel est votre système d'exploitation")
    lbl_reponse.configure(text="Le nom du/des dossier(s)")
    lbl_usr.configure(text="Votre nom d'utilisateur sur l'ordinateur")
    lbl_folders.configure(text="Le dossier de départ :")
    lbl_info.configure(text="Quand vous avez fini, appuyez sur Entrer")
    text1.configure(text="Vous n'avez pas entré de nom")
    text2.configure(text="Nous ouvrons le dossier...")
    l.config(text='Vous avez sélectionné le disque C')
    l2.config(text="Vous avez sélectionné un dossier")
    l3.configure(text="Vous avez sélectionné le système d'exploitation Windows")
    l4.configure(text="Vous avez séléctionné le système d'exploitation Linux")
    l5.config(text='Vous avez sélectionné le disque D')
    lbl_drive.configure(text="Quel est le nom du disque de départ ?")
    lbl_sys_infowin.configure(text="Le répertoire de base est: Ce PC/")
    lbl_sys_infolinux.configure(text="Le répertoire de base est: /home/")
    r1.configure(text="Documents")
    r2.configure(text="Téléchargements")
    r3.configure(text="Bureau")
    r4.configure(text="Images")
    r5.configure(text="Musique")
    r6.configure(text="Vidéos")
    bFullscreen.configure(text="Plein écran")
    rLinux.grid(row=1, column=2, sticky=tkinter.W)
    rWin.grid(row=1, column=1, sticky=tkinter.W)
    lbl_sys.grid(row=1, column=0, pady=5, padx=3)
    lbl_lang.grid_forget()
    bFr.grid_forget()
    bEng.grid_forget()
    txtlang.grid(row=15, column=0)
    bEngafter.grid(row=15, column=1)
    bFrafter.grid(row=15, column=2)

##When called it translates all the text in English
def translate_Eng():
    title.configure(text="Path creator")
    lbl_sys.configure(text="What's your OS")
    lbl_reponse.configure(text="The name of your folder(s)")
    lbl_usr.configure(text="Your computer username")
    lbl_folders.configure(text="The start folder :")
    lbl_info.configure(text="When you have done, press Enter key")
    text1.configure(text="You didn't entered a name")
    text2.configure(text="We are opening the folder...")
    l.config(text='You have selected the C drive')
    l2.config(text="You have selected a folder")
    l3.configure(text="You have selected the Windows environment")
    l4.configure(text="You have selected the Linux environment")
    l5.config(text='You have selected the D drive')
    lbl_drive.configure(text="What's the name of the Drive chosed")
    lbl_sys_infowin.configure(text="Your start path is: This PC/")
    lbl_sys_infolinux.configure(text="Your start path is: /home/")
    r1.configure(text="Documents")
    r2.configure(text="Downloads")
    r3.configure(text="Desktop")
    r4.configure(text="Images")
    r5.configure(text="Music")
    r6.configure(text="Videos")
    bFullscreen.configure(text="Fullscreen")
    rLinux.grid(row=1, column=2, sticky=tkinter.W)
    rWin.grid(row=1, column=1, sticky=tkinter.W)
    lbl_sys.grid(row=1, column=0, pady=5, padx=3)
    lbl_lang.grid_forget()
    bFr.grid_forget()
    bEng.grid_forget()
    txtlang.grid(row=15, column=0)
    bEngafter.grid(row=15, column=1)
    bFrafter.grid(row=15, column=2)

##When called it creates all the elements needed for creating folders in Windows environments
def print_selection_sys_Win():
    l.grid_forget()
    l3.grid_forget()
    l4.grid_forget()
    l5.grid_forget()
    l3.grid(row=12, column=0, padx=5)
    lbl_drive.grid(row=4, column=0, pady=5, padx=5)
    lbl_sys_infowin.grid(row=13, column=0, pady=5, padx=5)
    rC.grid(row=4, column=1, sticky=tkinter.W)
    rD.grid(row=4, column=2, sticky=tkinter.W)
    lbl_reponse.grid(row=2, column=0, pady=5, padx=3)
    lbl_usr.grid(row=3, column=0, pady=5, padx=5)
    lbl_folders.grid(row=5, column=0, pady=5, padx=5)
    directoryent.grid(row=2, column=1, pady=5, padx=5)
    comp_usr.grid(row=3, column=1, pady=5, padx=5)
    lbl_info.grid(row=14, column=0, pady=5, padx=5)
    r1.grid(row=5, column=1, sticky=tkinter.W)
    r2.grid(row=5, column=2, sticky=tkinter.W)
    r3.grid(row=6, column=1, sticky=tkinter.W)
    r4.grid(row=6, column=2, sticky=tkinter.W)
    r5.grid(row=7, column=1, sticky=tkinter.W)
    r6.grid(row=7, column=2, sticky=tkinter.W)

##When called it creates all the elements needed for creating folders in Linux environments
def print_selection_sys_Linux():
    l.grid_forget()
    l2.grid_forget()
    l3.grid_forget()
    l5.grid_forget()
    l4.grid(row=12, column=0, padx=5)
    lbl_sys_infolinux.grid(row=13, column=0, pady=5, padx=5)
    lbl_reponse.grid(row=2, column=0, pady=5, padx=3)
    lbl_usr.grid(row=3, column=0, pady=5, padx=5)
    lbl_folders.grid(row=5, column=0, pady=5, padx=5)
    directoryent.grid(row=2, column=1, pady=5, padx=5)
    comp_usr.grid(row=3, column=1, pady=5, padx=5)
    lbl_info.grid(row=14, column=0, pady=5, padx=5)
    r1.grid(row=5, column=1, sticky=tkinter.W)
    r2.grid(row=5, column=2, sticky=tkinter.W)
    r3.grid(row=6, column=1, sticky=tkinter.W)
    r4.grid(row=6, column=2, sticky=tkinter.W)
    r5.grid(row=7, column=1, sticky=tkinter.W)
    r6.grid(row=7, column=2, sticky=tkinter.W)
    rC.grid_forget()
    rD.grid_forget()
    lbl_drive.grid_forget()

##When called, it informs the user of the fact that's the C drive wich is selected
def exp_Cdrive():
    l2.grid_forget()
    l3.grid_forget()
    l4.grid_forget()
    l5.grid_forget()
    l.grid(row=12, column=0, padx=5)

##When called, it informs the user of the fact that's the D drive wich is selected
def exp_Ddrive():
    l.grid_forget()
    l2.grid_forget()
    l3.grid_forget()
    l4.grid_forget()
    l5.grid(row=12, column=0, padx=5)

##When called, the programm is in Fullscreen
def Toggle_Fullscreen():
    if window.attributes("-fullscreen") == True:
        window.attributes("-fullscreen", False)
    else:
        window.attributes("-fullscreen", True)

##When called, it close the programm
def Quit():
    window.destroy()



##Creating window with Tkinter module
window = tkinter.Tk()

##We set the window Title
window.title("Path Creator")

##We set the background color in hexadecimal
window.configure(background='#323232')

##We set the width and the height of the window
window.geometry('1280x720')



#Vars
comp_drive = tkinter.StringVar()
env = tkinter.StringVar()
sys = tkinter.StringVar()
lang = ""

##Title of the Window
title = tkinter.Label(window, text="", font=("", 23), background="#323232", fg="cyan")
title.grid(row=0, column=1, pady=12, padx=50)


## Labels
lbl_sys = tkinter.Label(window, text="", font=("", 15), background="#323232", fg="#ffffff")
lbl_sys.grid(row=1, column=0, pady=5, padx=3)
lbl_sys.grid_forget()
lbl_reponse = tkinter.Label(window, text="", font=("", 15), background="#323232", fg="#ffffff")
lbl_reponse.grid(row=2, column=0, pady=5, padx=3)
lbl_reponse.grid_forget()
lbl_usr = tkinter.Label(window, text="", font=("", 15), background="#323232", fg="#ffffff")
lbl_usr.grid(row=3, column=0, pady=5, padx=5)
lbl_usr.grid_forget()
lbl_drive = tkinter.Label(window, text="", font=("", 15), background="#323232", fg="#ffffff")
lbl_drive.grid(row=4, column=0, pady=5, padx=5)
lbl_drive.grid_forget()
lbl_folders = tkinter.Label(window, text="", font=("", 15), background="#323232", fg="#ffffff")
lbl_folders.grid(row=5, column=0, pady=5, padx=5)
lbl_folders.grid_forget()
text1 = tkinter.Label(window, text="", font=("", 15), background="#323232", fg="#ffffff")
text1.grid(row=8, column=1, pady=5, padx=5)
text1.grid_forget()
text2 = tkinter.Label(window, text="", font=("", 15), background="#323232", fg="#ffffff")
text2.grid(row=9, column=1, pady=5, padx=5)
text2.grid_forget()
text3 = tkinter.Label(window, text="", font=("", 15), background="#323232", fg="#ffffff")
text3.grid(row=10, column=1, pady=5, padx=5)
lsys = tkinter.Label(window, bg='#323232', text="", background="#323232", fg="#ffffff", font=("", 15))
lsys.grid(row=11, column=0, padx=5)
l = tkinter.Label(window, bg='#323232', text="", background="#323232", fg="#ffffff", font=("", 15))
l.grid(row=12, column=0, padx=5)
l.grid_forget()
l2 = tkinter.Label(window, bg='#323232', text="", background="#323232", fg="#ffffff", font=("", 15))
l2.grid(row=12, column=0, padx=5)
l2.grid_forget()
l3 = tkinter.Label(window, bg='#323232', text="", background="#323232", fg="#ffffff", font=("", 15))
l3.grid(row=12, column=0, padx=5)
l3.grid_forget()
l4 = tkinter.Label(window, bg='#323232', text="", background="#323232", fg="#ffffff", font=("", 15))
l4.grid(row=12, column=0, padx=5)
l4.grid_forget()
l5 = tkinter.Label(window, bg='#323232', text="", background="#323232", fg="#ffffff", font=("", 15))
l5.grid(row=12, column=0, padx=5)
l5.grid_forget()
lbl_sys_infowin = tkinter.Label(window, text="", background="#323232", fg="#ffffff", font=("", 15))
lbl_sys_infowin.grid(row=13, column=0, pady=5, padx=5)
lbl_sys_infowin.grid_forget()
lbl_sys_infolinux = tkinter.Label(window, text="", background="#323232", fg="#ffffff", font=("", 15))
lbl_sys_infolinux.grid(row=13, column=0, pady=5, padx=5)
lbl_sys_infolinux.grid_forget()
lbl_info = tkinter.Label(window, text="", font=("", 15), background="#323232", fg="#ffffff")
lbl_info.grid(row=14, column=0, pady=5, padx=5)
lbl_info.grid_forget()
lbl_lang = tkinter.Label(window, text="Select your language", font=("", 23), background="#323232", fg="#ffffff")
lbl_lang.grid(row=1, column=0, pady=5, padx=5)
txtlang = tkinter.Label(window, text="Languages", font=("", 23), background="#323232", fg="#ffffff")
txtlang.grid(row=15, column=0)
txtlang.grid_forget()


##Input as Entries
directoryent = tkinter.Entry(window, background="#323232", fg="#ffffff", font=("", 23))
directoryent.grid(row=2, column=1, pady=5, padx=5)
directoryent.grid_forget()
comp_usr = tkinter.Entry(window, background="#323232", fg="#ffffff", font=("", 23))
comp_usr.grid(row=3, column=1, pady=5, padx=5)
comp_usr.grid_forget()
directoryent.bind("<Return>", myfunc)
comp_usr.bind("<Return>", myfunc)


##Buttons
##Radio Buttons
rC = tkinter.Radiobutton(window, text="C:", variable=comp_drive, value="C", background="#323232", fg="green", font=("", 23), command=exp_Cdrive)
rC.grid(row=4, column=1, sticky=tkinter.W)
rC.grid_forget()
rD = tkinter.Radiobutton(window, text="D:", variable=comp_drive, value="D", background="#323232", fg="green", font=("", 23), command=exp_Ddrive)
rD.grid(row=4, column=2, sticky=tkinter.W)
rD.grid_forget()
r1 = tkinter.Radiobutton(window, text="", variable=env, value="Documents", background="#323232", fg="green", font=("", 23), command=print_selection2)
r1.grid(row=5, column=1, sticky=tkinter.W)
r1.grid_forget()
r2 = tkinter.Radiobutton(window, text="", variable=env, value="Downloads", background="#323232", fg="green", font=("", 23), command=print_selection2)
r2.grid(row=5, column=2, sticky=tkinter.W)
r2.grid_forget()
r3 = tkinter.Radiobutton(window, text="", variable=env, value="Desktop", background="#323232", fg="green", font=("", 23), command=print_selection2)
r3.grid(row=6, column=1, sticky=tkinter.W)
r3.grid_forget()
r4 = tkinter.Radiobutton(window, text="", variable=env, value="Pictures", background="#323232", fg="green", font=("", 23), command=print_selection2)
r4.grid(row=6, column=2, sticky=tkinter.W)
r4.grid_forget()
r5 = tkinter.Radiobutton(window, text="", variable=env, value="Music", background="#323232", fg="green", font=("", 23), command=print_selection2)
r5.grid(row=7, column=1, sticky=tkinter.W)
r5.grid_forget()
r6 = tkinter.Radiobutton(window, text="", variable=env, value="Videos", background="#323232", fg="green", font=("", 23), command=print_selection2)
r6.grid(row=7, column=2, sticky=tkinter.W)
r6.grid_forget()
rWin = tkinter.Radiobutton(window, text="Windows", variable=sys, value="Windows", background="#323232", fg="orangered", font=("", 23), command=print_selection_sys_Win)
rWin.grid(row=1, column=1, sticky=tkinter.W)
rWin.grid_forget()
rLinux = tkinter.Radiobutton(window, text="Linux", variable=sys, value="Linux", background="#323232", fg="orangered", font=("", 23), command=print_selection_sys_Linux)
rLinux.grid(row=1, column=2, sticky=tkinter.W)
rLinux.grid_forget()


##Simple Buttons
bEng = tkinter.Radiobutton(window, text="English", variable=lang, value="eng", background="#323232", fg="orange", font=("", 23), command=translate_Eng)
bEng.grid(row=1, column=1)
bFr = tkinter.Radiobutton(window, text="Français", variable=lang, value="fr", background="#323232", fg="orange", font=("", 23), command=translate_Fr)
bFr.grid(row=1, column=2)
bEngafter = tkinter.Radiobutton(window, text="English", variable=lang, value="eng", background="#323232", fg="orange", font=("", 23), command=translate_Eng)
bEngafter.grid(row=15, column=1)
bEngafter.grid_forget()
bFrafter = tkinter.Radiobutton(window, text="Français", variable=lang, value="fr", background="#323232", fg="orange", font=("", 23), command=translate_Fr)
bFrafter.grid(row=15, column=2)
bFrafter.grid_forget()


##Imporants Buttons
##
##          DON'T EVER IMAGINE REMOVE THEM OR HIDE THEM !!!!!!!
##
#####################################################################################
bFullscreen = tkinter.Button(window, text="[ ]", background="#323232", fg="red", font=("", 23), command=Toggle_Fullscreen)
bFullscreen.grid(row=0, column=3, sticky=tkinter.W)
bExit = tkinter.Button(window, text="X", background="#323232", fg="red", font=("", 23), command=Quit)
bExit.grid(row=0, column=4, sticky=tkinter.W)




##Start the app
window.mainloop()
