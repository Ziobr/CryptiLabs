# coding=utf-8
'''
Created on 26 апр. 2015 г.

@author: Ziobr
'''

from tkinter import *
from tkinter.ttk import *
from CryptoLabs.Stats import allDiGraphs, diGraph

class DiGraphsWindow(Frame):
    def __init__(self, parent, textData=''):
        Frame.__init__(self, parent, height = 800)
        self.parent = parent
        self.statsDict = allDiGraphs(textData)
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

class DiGraphLetterWindow(Frame):
    def __init__(self, parent, textData='', letter = ''):
        Frame.__init__(self, parent)
        self.parent = parent
        self.statsDict = diGraph(textData, letter)
        self.createGUI()
    def createGUI(self):
        row = 0
        for w in sorted(self.statsDict, key=self.statsDict.get, reverse=True):
            label1 = Label(self, text = w)
            label2 = Label(self, text = self.statsDict[w])
            label1.grid(row = row, column = 0)
            label2.grid(row = row, column = 1)
            row +=1
            
if __name__ == '__main__':
    root = Tk()
    #b = DiGraphsWindow(root, 'еищезщеыжхсхмвыдвеюээелдэмвигэрлюэяеюезузшувдиуэиишвсезхщэвзжхэфщекеюхилешеьвщэуштмвызчбвсбэрэжюусхизвдуоэриудемвглювсфвдхэлюебвсбэрмвювжелдэмвигэавщдюэюезхщщтниэидвфтхдхгьвэзчуищвщэвдхгекелесяеюхэюхилешеьвщэуввпшвфвщдезлюэгедеючрштмэзчбвсбэвэжгхьсеыеизвовщщеыдемгэлювсфвдхлеэрлюереьсвщээсхшэячэжеяюхьвщэвфэщэфхшцщчрюхжфвюезюхжфвовщэвьвихфчрэжеяюхьвщэыячшеячлесеящеюхилешеьвщэндемвгпдхжхсхмхзееяовмювжзчмхыщеишеьщхэщхлюхгдэгвлемдэзивксхювбхвдиуиэжзвидщчфлюэяшэьвщэвф')
    b = DiGraphLetterWindow(root, 'еищезщеыжхсхмвыдвеюээелдэмвигэрлюэяеюезузшувдиуэиишвсезхщэвзжхэфщекеюхилешеьвщэуштмвызчбвсбэрэжюусхизвдуоэриудемвглювсфвдхэлюебвсбэрмвювжелдэмвигэавщдюэюезхщщтниэидвфтхдхгьвэзчуищвщэвдхгекелесяеюхэюхилешеьвщэуввпшвфвщдезлюэгедеючрштмэзчбвсбэвэжгхьсеыеизвовщщеыдемгэлювсфвдхлеэрлюереьсвщээсхшэячэжеяюхьвщэвфэщэфхшцщчрюхжфвюезюхжфвовщэвьвихфчрэжеяюхьвщэыячшеячлесеящеюхилешеьвщэндемвгпдхжхсхмхзееяовмювжзчмхыщеишеьщхэщхлюхгдэгвлемдэзивксхювбхвдиуиэжзвидщчфлюэяшэьвщэвф', 'в')
    b.pack()
    root.mainloop()            