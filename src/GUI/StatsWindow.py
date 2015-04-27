# coding=utf-8
'''
Created on 22 апр. 2015 г.

@author: Ziobr
'''

from tkinter import *
from tkinter.ttk import *
from GUI.DiGraphsWindow import DiGraphLetterWindow

class StatsWindow(Frame):
    def __init__(self, parent, textData = ''):
        Frame.__init__(self, parent)
        self.textData = textData
        self.labels1 = []
        self.labels2 = []
        self.buttons = []
        self.createGUI()
    def createGUI(self):
        chardict = {}
        chars = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        for char in chars:
            chardict[char] = self.textData.count(char)
        row = 0
        for w in sorted(chardict, key=chardict.get, reverse=True):
            print (w, chardict[w])
            self.labels1.append(Label(self, text = w))
            self.labels2.append(Label(self, text = chardict[w]))
            self.labels1[row].grid(row = row, column = 0)
            self.labels2[row].grid(row = row, column = 1)
            #self.buttons.append(Button(self, text = w))
            #self.buttons[row].grid(row = row, column = 2)
            row +=1
        #for button in self.buttons:
        #    letter = button['text']
        #    print(letter)
        #    button['command'] = lambda : self.showDiGraphs(letter)
    def showDiGraphs(self, letter):
        print(letter)
        self.diGraphsForm = Toplevel()
        self.diGraphsForm.wm_title('Биграммы')
        #self.diGraphsForm.protocol("WM_DELETE_WINDOW", self.onClose)
        diGraphs = DiGraphLetterWindow(self.diGraphsForm, self.textData, letter)
        diGraphs.pack()
        diGraphs.createGUI()  
        
                    
if __name__ == '__main__':
    root = Tk()
    b = StatsWindow(root, 'еищезщеыжхсхмвыдвеюээелдэмвигэрлюэяеюезузшувдиуэиишвсезхщэвзжхэфщекеюхилешеьвщэуштмвызчбвсбэрэжюусхизвдуоэриудемвглювсфвдхэлюебвсбэрмвювжелдэмвигэавщдюэюезхщщтниэидвфтхдхгьвэзчуищвщэвдхгекелесяеюхэюхилешеьвщэуввпшвфвщдезлюэгедеючрштмэзчбвсбэвэжгхьсеыеизвовщщеыдемгэлювсфвдхлеэрлюереьсвщээсхшэячэжеяюхьвщэвфэщэфхшцщчрюхжфвюезюхжфвовщэвьвихфчрэжеяюхьвщэыячшеячлесеящеюхилешеьвщэндемвгпдхжхсхмхзееяовмювжзчмхыщеишеьщхэщхлюхгдэгвлемдэзивксхювбхвдиуиэжзвидщчфлюэяшэьвщэвф')
    b.pack()
    root.mainloop()            