# coding=utf-8
'''
Created on 28 апр. 2015 г.

@author: Ziobr
'''
from tkinter import *
from tkinter.ttk import *
from CryptoLabs.Stats import allTriGraphs, diGraph

class TriGraphsWindow(Frame):
    def __init__(self, parent, textData=''):
        Frame.__init__(self, parent, height = 800)
        self.parent = parent
        self.statsDict = allTriGraphs(textData)
        self.createGUI()
    def createGUI(self):
        scrollbar = Scrollbar(self.parent)
        scrollbar.pack(side = RIGHT, fill = Y)
        listbox = Listbox(self.parent, yscrollcommand=scrollbar.set, width = 10)
        row = 0
        for w in sorted(self.statsDict, key=self.statsDict.get, reverse=True):
            listbox.insert(END, w + ':' + str(self.statsDict[w]))
        listbox.pack(side=LEFT, fill=BOTH)
        scrollbar.config(command=listbox.yview)

if __name__ == '__main__':
    root = Tk()
    b = TriGraphsWindow(root, 'еищезщеыжхсхмвыдвеюээелдэмвигэрлюэяеюезузшувдиуэиишвсезхщэвзжхэфщекеюхилешеьвщэуштмвызчбвсбэрэжюусхизвдуоэриудемвглювсфвдхэлюебвсбэрмвювжелдэмвигэавщдюэюезхщщтниэидвфтхдхгьвэзчуищвщэвдхгекелесяеюхэюхилешеьвщэуввпшвфвщдезлюэгедеючрштмэзчбвсбэвэжгхьсеыеизвовщщеыдемгэлювсфвдхлеэрлюереьсвщээсхшэячэжеяюхьвщэвфэщэфхшцщчрюхжфвюезюхжфвовщэвьвихфчрэжеяюхьвщэыячшеячлесеящеюхилешеьвщэндемвгпдхжхсхмхзееяовмювжзчмхыщеишеьщхэщхлюхгдэгвлемдэзивксхювбхвдиуиэжзвидщчфлюэяшэьвщэвф')
    b.pack()
    root.mainloop()            