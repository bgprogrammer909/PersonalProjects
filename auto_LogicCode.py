import os, shutil
#location of target path
path = r"C:/Users/ACER/Desktop/test/"

#checking if sorting folder exists
type=["Document","Image","Diagram"]
# things=os.listdir(path)
new=[]
#filter files only
for files in os.listdir(path):
    if not os.path.isdir(path+files):
        new.append(files)
#looping to find if folders like that exists 
# othwerwise make it
for i in range(0,len(type)):
    if not os.path.exists(path + type[i]):
        os.makedirs(path+type[i])

#now sorting it in respective file
for file in new:
#check extension in name of file and if path inside desired foolder exist
    if (".doc" in file or ".pdf" in file) and not os.path.exists(path +"Document/"+file):
    #moves the file insde desired folder
        shutil.move(path + file, path +"Document/"+file)
#check extension in name of file and if path inside desired foolder exist
    if (".jpg" in file or ".png" in file or ".jpeg" in file) and not os.path.exists(path+"Image/"+file):
    #moves the file insde desired folder
        shutil.move(path+file, path+"Image/"+file) 
    
#check extension in name of file and if path inside desired foolder exist
    if ".drawio" in file and not os.path.exists(path+"Diagram/"+file):
    #moves the file insde desired folder
        shutil.move(path+file, path+"Diagram/"+file) 
    
        
