# coding=utf-8
'''
Created on 22 апр. 2015 г.

@author: Ziobr
'''

from tkinter import *
from tkinter.ttk import *

class StatsWindow(Frame):
    def __init__(self, parent, textData = ''):
        Frame.__init__(self, parent)
        self.textData = textData
        self.createGUI()
    def createGUI(self):
        chardict = {}
        chars = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        for char in chars:
            chardict[char] = self.textData.count(char)
        row = 0
        for w in sorted(chardict, key=chardict.get, reverse=True):
            print (w, chardict[w])
            label1 = Label(self, text = w)
            label2 = Label(self, text = chardict[w])
            label1.grid(row = row, column = 0)
            label2.grid(row = row, column = 1)
            row +=1
            
if __name__ == '__main__':
    root = Tk()
    b = StatsWindow(root, 'еищезщеыжхсхмвыдвеюээелдэмвигэрлюэяеюезузшувдиуэиишвсезхщэвзжхэфщекеюхилешеьвщэуштмвызчбвсбэрэжюусхизвдуоэриудемвглювсфвдхэлюебвсбэрмвювжелдэмвигэавщдюэюезхщщтниэидвфтхдхгьвэзчуищвщэвдхгекелесяеюхэюхилешеьвщэуввпшвфвщдезлюэгедеючрштмэзчбвсбэвэжгхьсеыеизвовщщеыдемгэлювсфвдхлеэрлюереьсвщээсхшэячэжеяюхьвщэвфэщэфхшцщчрюхжфвюезюхжфвовщэвьвихфчрэжеяюхьвщэыячшеячлесеящеюхилешеьвщэндемвгпдхжхсхмхзееяовмювжзчмхыщеишеьщхэщхлюхгдэгвлемдэзивксхювбхвдиуиэжзвидщчфлюэяшэьвщэвф')
    b.pack()
    root.mainloop()            