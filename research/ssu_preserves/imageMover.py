import os.path
from shutil import copyfile
#import shutil


file = open("ImagesToMove.txt", "r")
images = list(file)
newImages = []
hit = False

loc = "nothing/"

for i in range (0, len(images)):
    #print(images[i])
    temp = ""
    for name in images[i]:
        if(hit == True):
            #print(name)
            temp = temp + name
        if(name == "/"):
            hit = True
    hit = False
    newImages.append(loc + temp)
    print(newImages[i])
    try:
        #copyfile(("images/" + images[i]).rstrip(), ("images/" + newImages[i]).rstrip())
        os.remove(("images/" + images[i]).rstrip())
    except:
        print("images/")
        print(images[i].rstrip())
        print(" not found")
