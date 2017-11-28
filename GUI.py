
from __future__ import print_function
from Tkinter import *
import gui
from SVN.SmartAIP.CSVDiff.GetFromDB import get_desc

window = gui.Window("Enter The Layout Number",layout="pack")
def onok():
    #get_desc('12345'
    #runSingleInAll()

def showGUI():

    window.pack(side=TOP, padx=100, pady=30)


    entry = Entry(window, width=40)
    entry.pack(side=TOP,padx=10,pady=10)

    Button(window, width=30, text='Check Duplicates', command=onok).pack(side=TOP, padx=20, pady=20)
    window.mainloop()


showGUI()