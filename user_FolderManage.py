#importing required modules
from tkinter import *
from tkinter import filedialog
path=r""
#creating window for user
root=Tk()
root.config(bg="#f0f0f0")
root.geometry("500x500+400+0")
root.resizable(0,0)
#functions--------------------------------------------------
def verify():
    usr=user.get()
    pas=pwd.get()
    print(usr,pas)
def file_window():
    global path
    find=filedialog.askdirectory() 
    print(find)
    path=find+"/"
    print(path)
#------------------------------------------------------------
#login

frame=Frame(root)
#inside frame
a=Label(frame,text="username",font=("Helvetica", 10), fg="#333", bg="#f0f0f0")
user=Entry(frame)
b=Label(frame,text="password",font=("Helvetica", 10), fg="#333", bg="#f0f0f0")
pwd=Entry(frame)
#widget place
Label(frame,text="Login",font=("Helvetica", 18, "bold"), fg="#333", bg="#f0f0f0").grid(row=0,column=1)
Button(frame,text="submit",command=verify,font=("Helvetica", 8), fg="#333", bg="#f0f0f0").grid(row=3,column=1)
a.grid(row=1,column=0)
user.grid(row=1,column=1)
b.grid(row=2,column=0)
pwd.grid(row=2,column=1)
frame.pack()
#database


#GUI---------------------------------------------------------
#labels
# heading=Label(root,text="FILE MANAGER",font=("Helvetica", 18, "bold"), fg="#333", bg="#f0f0f0")
# folder_finding=Button(text="choose folder",command=file_window)

# heading.pack()
# folder_finding.pack()



#------------------------------------------------------------
root.mainloop()