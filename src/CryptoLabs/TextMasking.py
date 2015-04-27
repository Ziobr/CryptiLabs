# coding=utf-8
'''
Created on 02 апр. 2015 г.

@author: Ziobr
'''
import codecs

def maskText(text='', symbolForReplace='', symbolToShow=''):
    intab = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    outtab = ''
    for s in intab:
        if s == symbolForReplace:
            outtab = outtab + symbolToShow
        else:
            outtab = outtab + '*'
    translationTab = str.maketrans(intab, outtab)
    return text.translate(translationTab)

def multMaskText (text = '', intab='', outtab=''):
    translationTab = str.maketrans(intab, outtab)
    return text.translate(translationTab)

if __name__ == '__main__':
    f = codecs.open('..\data\code.txt', 'r', 'utf-8')
    text = f.read()
    print(text)
    print(maskText(text, 'и', 'я'))
    f.close()