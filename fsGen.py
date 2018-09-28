import random
import os
import sys

base = sys.argv[1]
count = int(sys.argv[2])
if(len(sys.argv) == 4):
        size = int(sys.argv[3])
        mode = "fixed"


dirs = []
dirs.append(base)
dirCount = 0
fileCount= 0
exts = ["txt","exe","jpg","docx","mp3","mp4"]

def Roll():
        if (random.randint(1,41) <= 3):
                global dirCount
                dirCount+=1
                objType = "dir"
        else:
                global fileCount
                fileCount+=1
                objType = "file"
        return objType

def makeDir(int,parent):
        path = os.path.join(parent,str(int))
        os.mkdir(path)
        dirs.append(path)

def makeFileR(int,parent):
        size = random.randint(1024,1024000)
        if (size > 1022000):
                size = random.randint(1024,1024000000)
        path = os.path.join(parent,str(int) + "." + random.choice(exts))
        f = open(path,"w")
        f.write(os.urandom(size))
        f.close()

def makeFile(int,parent):
        path = os.path.join(parent,str(int) + "." + random.choice(exts))
        f = open(path,"w")
        f.write(os.urandom(size))
        f.close()

if(mode == "random"):
	i = 1
	while i < count+1:
        #for i in range(1,count+1):
                print i
                parent = random.choice(dirs)
                if (Roll() == "dir"):
                        makeDir(i,parent)
                else:
                        makeFileR(i,parent)
		i+=1

else:
	i = 1
	while i < count+1:
        #for i in range(1,count+1):
                print i
                parent = random.choice(dirs)
                if (Roll() == "dir"):
                        makeDir(i,parent)
                else:
                        makeFile(i,parent)
		i+=1

print str(fileCount) + " Files\r\n" + str(dirCount) + " Directories"
