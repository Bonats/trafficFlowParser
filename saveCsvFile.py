import csv
from tkinter import filedialog
from tkinter import *

def saveFile(finalMainAnswer,direction,streetName):

    myFile = open(direction+'_'+streetName+'.csv', 'w')
    with myFile:
        writer = csv.writer(myFile,sys.stdout, lineterminator='\n')
        writer.writerows(finalMainAnswer)

def saveDataSet(fileName,finalMainAnswer):

    myFile = open(fileName+'.csv', 'w')
    with myFile:
        writer = csv.writer(myFile,sys.stdout, lineterminator='\n')
        writer.writerows(finalMainAnswer)
