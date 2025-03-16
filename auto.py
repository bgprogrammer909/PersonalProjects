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
