"""
PZTOOLS 0.2
DECEMBER 1 2022
"""

import tkinter.ttk
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
import os
import send2trash as s2t
dir = f"C:\\Users\\{os.getlogin()}\\Zomboid\\mods"
#customdir = ""
dirstate = 0
state = 0


def inform(message):
    label_inform.configure(text=message)

def exebuttonstatus(status):
    button_savechanges.configure(state=status)

def addbutton():
    global state
    state = 1
    inform("Create a new mod")
    button_savechanges.configure(text="Create")
    exebuttonstatus('enabled')

def removebutton():
    global state
    state = 2
    inform("Remove an existing mod")
    button_savechanges.configure(text="Remove")
    exebuttonstatus('enabled')

def removefolder():
    if listbox_modlist.curselection():
        name = listbox_modlist.selection_get()
        s2t.send2trash(f"{dir}\\{name}")
        print(f"Mod {name} has been deleted.")
        refreshList()
    else:
        inform("Error: select a folder to delete")

def execute():
    if state == 1:
        newMod()
    if state == 2:
        removefolder()
    if state == 0:
        exebuttonstatus('disabled')

def cancel():
    global state
    state = 0
    inform("Cancelled")
    exebuttonstatus('disabled')

def gotofolder():
    if listbox_modlist.curselection():
        os.system(f"start {dir}\\{listbox_modlist.selection_get()}")
    else:
        os.system(f"start {dir}")

"""
def settings():

    def getcustomfolder():
        cusdir = filedialog.askdirectory()
        entry_customdirectory.insert(0, cusdir)
    setroot = Tk()
    setroot.resizable(False, False)
    setroot.title("PZTools - Settings")
    setroot.iconbitmap("icon.ico")
    setroot.geometry("400x400")

    #def apply():


    ## Widgets ##
    ## Label Frames
    labelframe_directory = Labelframe(setroot, text="Directory", width=380, height=100)
    ## Labels
    label_moddirectory = Label(setroot, text="Mod Folder Directory")
    ## Radio Buttons
    radiobutton_default = Radiobutton(setroot, text=f"Default ({dir})", variable=dirstate, value=1, command=lambda:[entry_customdirectory.configure(state='disabled'),button_customdirectory.configure(state='disabled')])
    radiobutton_custom = Radiobutton(setroot, text="Custom", variable=dirstate, value=2, command=lambda:[entry_customdirectory.configure(state='enabled'),button_customdirectory.configure(state='enabled')])
    ## Entry Boxes
    entry_customdirectory = Entry(setroot, width=30)
    # Buttons
    button_customdirectory = Button(setroot, text="Select Folder", command=getcustomfolder)
    button_apply = Button(setroot, text="Save Changes")
    # Initialization
    labelframe_directory.place(relx=0.025, rely=0.025)
    radiobutton_default.place(relx=0.05, rely=0.1)
    radiobutton_custom.place(relx=0.05, rely=0.15)
    entry_customdirectory.place(relx=0.25, rely=0.15)
    button_customdirectory.place(relx=0.75, rely=0.1455)
    button_apply.place(relx=0.75, rely=0.9)
""" # SETTINGS FUNCTION

def newMod():
    if os.path.exists(dir):
        name = entry_name.get()
        id = entry_id.get()
        entry_desc.get()
        if name != "":
            os.chdir(dir)
            os.mkdir(name)
            if os.path.exists(f"{dir}\\{name}"):
                os.chdir(f"{dir}\\{name}")
                open('mod.info', 'w').write(f"name={name}\nid={id}\ndescription={entry_desc}")
                print(f"Mod {name} folder has been created successfully.")
                refreshList()
                button_savechanges.configure(text="Save Changes")
        elif name == "":
            inform("Error: Please name your folder")
        elif name == os.path.exists(f"{dir}\\{name}"):
            inform("Error: A folder by the same name already exists")

def refreshList():
    listbox_modlist.delete(0, END)
    for f in os.listdir(dir):
        if os.path.exists(f'{os.path.join(dir, f)}\\mod.info'):
            listbox_modlist.insert(END, f)

# Window parameters
root = Tk()
root.geometry("400x400")
root.resizable(False, False)
root.title("PZTools 0.2")
root.iconbitmap("icon.ico")

# Widget assets
add = PhotoImage(file='assets/add.png')
remove = PhotoImage(file='assets/remove.png')
delete = PhotoImage(file='assets/delete.png')
refresh = PhotoImage(file='assets/refresh.png')
cog = PhotoImage(file='assets/cog.png')
fold = PhotoImage(file='assets/fol.png')
fopen = PhotoImage(file='assets/openfolder.png')
run = PhotoImage(file='assets/run.png')

# The widgets
## Label Frames
labelframe_info = LabelFrame(text="Information", borderwidth=0, width=200, height=330)
## Labels
label_modlist = Label(root, text="Existing Mod Folders")
label_name = Label(labelframe_info, text="Name")
label_id = Label(labelframe_info, text="ID")
label_desc = Label(labelframe_info, text="Description")
label_inform = Label(root, text="")
## Entry Boxes
entry_name = Entry(labelframe_info, width=16)
entry_id = Entry(labelframe_info, width=16)
entry_desc = Entry(labelframe_info, width=24)
## Buttons
button_add = Button(root, text="Add", image=add, command=addbutton)
button_remove = Button(root, text="Remove", image=remove, command=removebutton)
button_refresh = Button(root, text="Refresh", image=refresh, command=lambda:[refreshList(),inform("Mod list has been refreshed.")])
button_config = Button(root, text="Settings", image=cog, command=lambda:[inform("Work in progress")])
button_savechanges = Button(labelframe_info, text="Save Changes", command=execute)
button_folder = Button(root, image=fold, command=gotofolder)
button_cancel = Button(labelframe_info, text="Cancel", command=cancel)
## List Box
listbox_modlist = Listbox(root, width=25, height=20, borderwidth=0)

# Initialization
label_modlist.place(relx=0.05, rely=0.074)
labelframe_info.place(relx=0.45, rely=0.108)
label_name.place(relx=0.035, rely=0.074)
label_id.place(relx=0.035, rely=0.148)
label_desc.place(relx=0.035, rely=0.222)
label_inform.place(relx=0, rely=0.95)
entry_name.place(relx=0.4, rely=0.074)
entry_id.place(relx=0.4, rely=0.148)
entry_desc.place(relx=0.05, rely=0.310)
button_add.place(relx=0,rely=0)
button_remove.place(relx=0.062, rely=0)
button_refresh.place(relx=0.124, rely=0)
button_config.place(relx=0.187, rely=0)
button_savechanges.place(relx=0.025,rely=0.9)
button_folder.place(relx=0.249, rely=0.0)
button_cancel.place(relx=0.45, rely=0.9)
listbox_modlist.place(relx=0.05, rely=0.124)

for folder in os.listdir(dir):
    if os.path.exists(f'{os.path.join(dir, folder)}\\mod.info'):
        listbox_modlist.insert(END, folder)
exebuttonstatus('disabled')
root.mainloop()

