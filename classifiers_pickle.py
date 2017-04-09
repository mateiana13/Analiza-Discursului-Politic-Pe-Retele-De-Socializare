from pickle import dump
from pickle import load

def savestate(clasificator,filename):
	f=open(filename,'wb')
	dump(clasificator,f)
	f.close()

def loadstate(filename):
	f=open(filename,'rb')
	clasificator=load(f)
	f.close()
	return clasificator


	