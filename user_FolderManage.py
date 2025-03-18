#importing required modules
from tkinter import *
from tkinter import filedialog
path=r""
#creating window for user
root=Tk()
root.config(bg="#f0f0f0")
root.geometry("500x700+0+0")
root.resizable(0,0)
#functions--------------------------------------------------
def file_window():
    global path
    find=filedialog.askdirectory() 
    print(find)
    path=find+"/"
    print(path)
#------------------------------------------------------------


#GUI---------------------------------------------------------
#labels
heading=Label(root,text="FILE MANAGER",font=("Helvetica", 18, "bold"), fg="#333", bg="#f0f0f0")
folder_finding=Button(text="choose folder",command=file_window)

heading.pack()
folder_finding.pack()



#------------------------------------------------------------
root.mainloop()