import os, shutil
#location of target path
path = r"C:/Users/ACER/Desktop/test/"

#checking if sorting folder exists
type=["Document","Image","Diagram"]

#looping to find if folders like that exists 
# othwerwise make it
for i in range(0,len(type)):
    if not os.path.exists(path + type[i]):
        os.makedirs(path+type[i])

#now sorting it in respective file
for file in os.listdir(path):
    if "_python" in file and not os.path.exists(path +"Document/"+file):
        shutil.move(path + file, path +"Document/"+file)
    