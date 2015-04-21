# coding=utf-8
'''
Created on 21 апр. 2015 г.

@author: Ziobr
'''
from tkinter import *
from tkinter.ttk import *

class SubstituteWindow(Frame):
    def __init__(self, parent, substituteDict):
        Frame.__init__(self, parent)
        self.substituteDict = substituteDict
        self.substituteFields ={}
        self.createGUI()
        
    def createGUI(self):
        row = 0
        for key in sorted(self.substituteDict):
            label = Label(self, text = key)
            label.grid(row = row, column = 0)
            #self.substituteDict[key].trace('w', self.entryupdate)
            self.substituteFields[key] = Entry(self, width = 30, textvariable = self.substituteDict[key])
            self.substituteFields[key].grid(row = row, column = 1)
            row+=1
    #def entryupdate(self, *args):
    #        print(self.substituteDict['а'].get())

if __name__ == '__main__':
    root = Tk()
    subst = {'а':StringVar(),
             'б':StringVar(),
             'в':StringVar(),
             'г':StringVar(),
             'д':StringVar(),
             'е':StringVar(),
             'ё':StringVar(),
             'ж':StringVar(),
             'з':StringVar(),
             'и':StringVar(),
             'й':StringVar(),
             'к':StringVar(),
             'л':StringVar(),
             'м':StringVar(),
             'н':StringVar(),
             'о':StringVar(),
             'п':StringVar(),
             'р':StringVar(),
             'с':StringVar(),
             'т':StringVar(),
             'у':StringVar(),
             'ф':StringVar(),
             'х':StringVar(),
             'ц':StringVar(),
             'ч':StringVar(),
             'ш':StringVar(),
             'щ':StringVar(),
             'ъ':StringVar(),
             'ы':StringVar(),
             'ь':StringVar(),
             'э':StringVar(),
             'ю':StringVar(),
             'я':StringVar(),
             }
    
    for key in subst.keys():
        subst[key].set('*')
    b = SubstituteWindow(root, subst)
    b.pack()
    root.mainloop()    