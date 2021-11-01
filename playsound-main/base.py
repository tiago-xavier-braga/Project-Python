import os

from playsound import playsound


def Directory():
	rootDir = "./music"
	for dirName, subdirList, fileList in os.walk(rootDir):
		for fname in fileList:
			files = fileList
	j = 0
	local = []
	for i in fileList:
		local.append(dirName + '/' + fileList[j])
		j += 1
	
	return dirName, local
	
def Play(object):
	j = 0
	for x in object[1]:
		playsound(object[1][j], block=True)
		j += 1

def Render(object):
	
	print("\nMusic album: " + object[0] + "\n")
	for x in object[1]:
		print(x)
	
	Play(object)

Render(Directory())
