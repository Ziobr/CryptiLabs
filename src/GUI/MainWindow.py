# coding=utf-8
'''
Created on 03 апр. 2015 г.

@author: Ziobr
'''
import codecs
from tkinter import *
from tkinter.ttk import *
from CryptoLabs.TextMasking import maskText, multMaskText
from GUI.SubstituteWindow import SubstituteWindow
from GUI.StatsWindow import StatsWindow

class MainWindow(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.textData= ''
        self.subsituteForm = None
        self.statsForm = None
        self.subsituteDict = {'а':StringVar(),
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
        self.createGUI()
        self.loadText()
        self.loadSubstituteForm()
        self.loadStatsForm()
    def createGUI(self):
        self.initTextArea = Frame(self, height = 50, width = 300)
        self.textArea = Frame(self, height = 50, width = 300)
        self.initText = Text(self.initTextArea, wrap=CHAR, state = DISABLED)
        self.initText.pack()
        self.text = Text(self.textArea, wrap=CHAR, state = DISABLED)
        self.text.pack()
        self.scrollbar = Scrollbar(self.textArea)
        self.loadButton = Button(self, text = 'Заменить', command = self.dummyFunc)
        self.resetButton = Button(self, text = 'Сбросить', command = self.resetData)
        self.initTextArea.grid(row = 1, column = 1)
        self.textArea.grid(row = 1, column = 2)
        self.loadButton.grid(row = 2, column = 1)
        self.resetButton.grid(row = 2, column = 2)
        self.parent.protocol("WM_DELETE_WINDOW", self.onClose)
    def onClose(self):
        self.subsituteForm.quit()
        self.quit()
        self.parent.quit()
    def loadText(self):
        f = codecs.open('..\data\code.txt', 'r', 'utf-8')
        self.textData = f.read()
        self.initText.config(state = NORMAL)
        self.initText.delete(1.0, END)
        self.initText.insert(1.0, self.textData)
        self.initText.config(state = DISABLED)
    def loadSubstituteForm(self):
        for key in self.subsituteDict.keys():
            self.subsituteDict[key].set('*')
        self.subsituteForm = Toplevel()
        self.subsituteForm.protocol("WM_DELETE_WINDOW", self.onClose)
        subst = SubstituteWindow(self.subsituteForm, self.subsituteDict, self.textData)
        subst.showStats()
        subst.pack()
    def loadStatsForm(self):
        self.statsForm = Toplevel()
        self.statsForm.protocol("WM_DELETE_WINDOW", self.onClose)
        stats = StatsWindow(self.statsForm, self.textData)
        stats.pack()
                
    def printDict(self):
        for i in sorted(self.subsituteDict):
            print(i, self.subsituteDict[i].get())
    def resetData(self):
        for i in self.s.substituteFields:
            self.s.substituteFields[i].delete(0, END)
            self.s.substituteFields[i].insert(0, "*")
        self.dummyFunc()
    def dummyFunc(self):
        intab = ''
        outtab = ''
        for i in sorted(self.subsituteDict):
            intab = intab + i
            outtab = outtab + self.subsituteDict[i].get()
        self.resultText = multMaskText(self.textData, intab, outtab)
        #self.resultText = maskText(self.textData, self.inputReplaceWhat.get(), self.inputReplaceTo.get())
        self.text.config(state = NORMAL)
        self.text.delete(1.0, END)
        self.text.insert(1.0, self.resultText)
        self.text.config(state = DISABLED)

if __name__ == '__main__':
    root = Tk()
    b = MainWindow(root)
    b.pack()
    root.mainloop()    