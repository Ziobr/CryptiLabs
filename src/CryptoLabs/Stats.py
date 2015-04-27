# coding=utf-8
'''
Created on 26 апр. 2015 г.

@author: Ziobr
'''

def diGraph (textData = '', letter = ''):
    statsDict = {}
    current = 0
    for symbol in textData:
        if symbol == letter:
            if current > 0:
                if not((textData[current-1]+letter) in statsDict.keys()):
                    if textData.count(textData[current-1]+letter) > 0:
                        statsDict[textData[current-1]+letter] = textData.count(textData[current-1]+letter)
            if current < len(textData)-1:
                if not((letter+textData[current+1]) in statsDict.keys()):
                    if textData.count(letter+textData[current+1]) > 0:
                        statsDict[letter+textData[current+1]] = textData.count(letter+textData[current+1])
        current +=1
    return statsDict

def allDiGraphs (textData = ''):
    statsDict = {}
    for letter in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
        statsDict.update(diGraph(textData, letter))
    return statsDict

def allTriGraphs (textData = ''):
    statsDict = {}
    current = 0
    for symbol in textData:
        if current < len(textData)-2:
            if not((symbol+textData[current+1]+textData[current+2]) in statsDict.keys()):
                if textData.count(symbol+textData[current+1]+textData[current+2]) > 0: 
                    statsDict[symbol+textData[current+1]+textData[current+2]] = textData.count(symbol+textData[current+1]+textData[current+2])
        current +=1
    return statsDict

if __name__ == '__main__':
    letter = 'в'
    textData = 'еищезщеыжхсхмвыдвеюээелдэмвигэрлюэяеюезузшувдиуэиишвсезхщэвзжхэфщекеюхилешеьвщэуштмвызчбвсбэрэжюусхизвдуоэриудемвглювсфвдхэлюебвсбэрмвювжелдэмвигэавщдюэюезхщщтниэидвфтхдхгьвэзчуищвщэвдхгекелесяеюхэюхилешеьвщэуввпшвфвщдезлюэгедеючрштмэзчбвсбэвэжгхьсеыеизвовщщеыдемгэлювсфвдхлеэрлюереьсвщээсхшэячэжеяюхьвщэвфэщэфхшцщчрюхжфвюезюхжфвовщэвьвихфчрэжеяюхьвщэыячшеячлесеящеюхилешеьвщэндемвгпдхжхсхмхзееяовмювжзчмхыщеишеьщхэщхлюхгдэгвлемдэзивксхювбхвдиуиэжзвидщчфлюэяшэьвщэвф'
    #print(diGram(textData, letter))
    #print(allDiGraphs(textData))
    print(allTriGraphs(textData))