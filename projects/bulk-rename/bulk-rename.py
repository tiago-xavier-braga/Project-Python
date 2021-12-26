import os

def RenameFiles(path, Newfilename):
    os.chdir(path)
    listfiles = os.listdir()
    for i in range(len(os.listdir())):
        os.renames(listfiles[i], Newfilename + str(i))
