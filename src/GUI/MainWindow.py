# coding=utf-8
'''
Created on 03 апр. 2015 г.

@author: Ziobr
'''
import codecs
from tkinter import *
from tkinter.ttk import *
from CryptoLabs.TextMasking import maskText

class MainWindow(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.createGUI()
    def createGUI(self):
        self.inputReplaceWhat = Entry(self, width = 10)
        self.inputReplaceTo = Entry(self, width = 10)
        self.initTextArea = Frame(self, height = 50, width = 300)
        self.textArea = Frame(self, height = 50, width = 300)
        self.initText = Text(self.initTextArea, wrap=CHAR, state = DISABLED)
        self.initText.pack()
        self.text = Text(self.textArea, wrap=CHAR, state = DISABLED)
        self.text.pack()
        #self.scrollbar = Scrollbar(self.textArea)
        self.loadButton = Button(self, text = 'Загрузить', command = self.dummyFunc)
        self.inputReplaceWhat.grid(row = 1, column = 1)
        self.inputReplaceTo.grid(row = 1, column = 2)
        self.initTextArea.grid(row = 2, column = 1)
        self.textArea.grid(row = 2, column = 2)
        self.loadButton.grid(row = 3, column = 1)
    def dummyFunc(self):
        f = codecs.open('..\..\Шифр.txt', 'r', 'utf-8')
        text = f.read()
        self.initText.config(state = NORMAL)
        self.initText.delete(1.0, END)
        self.initText.insert(1.0, text)
        self.initText.config(state = DISABLED)
        self.resultText = maskText(text, self.inputReplaceWhat.get(), self.inputReplaceTo.get())
        self.text.config(state = NORMAL)
        self.text.delete(1.0, END)
        self.text.insert(1.0, self.resultText)
        self.text.config(state = DISABLED)

if __name__ == '__main__':
    root = Tk()
    b = MainWindow(root)
    b.pack()
    root.mainloop()    