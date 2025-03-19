#importing required modules
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import Toplevel
path=r""
#creating window for user
root=Tk()
root.config(bg="#f0f0f0")
root.geometry("500x500+400+0")
root.resizable(0,0)
att=0
#functions--------------------------------------------------
def verify():
    global att
    usr=user.get()
    pas=pwd.get()
    if usr=="Suchit" and pas=="pythonisbest":
        root.destroy()
        att=0
        roots=Toplevel()
        roots.config(bg="#f0f0f0")
        roots.geometry("500x500+400+0")
        roots.resizable(0,0)
    else:
        att+=1
        messagebox.showerror("oops!",f"invalid username or password,{3-att} attempts left")
        if att==3:
            root.destroy()
        
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