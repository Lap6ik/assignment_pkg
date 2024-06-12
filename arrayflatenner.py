'''
__author__= Tatiana Lapshina, __version__=1.1, 10/03/2021
This code below will flatten array(list or tuple) of numbers:
example: (1,18,(19,6,(100,32)))-->[1, 18, 19, 6, 100, 32]
final array will be a list 
if the argument is number or string:
example: "hnksh"-->["hnksh"]
example: 999.14 -->[999.14]
KeyErrors when dictionary passed
'''
from threading import Thread


def flattenArray(element):
    b=[]
    b= flattenElement([],element)
    return b


def flattenElement(partEl,element):
    if hasattr(element,'__len__') and not isinstance(element, str):
        for i in range(len(element)):
            thread=Thread(target=flattenElement, args=[partEl,element[i]])
            thread.start()
            thread.join()
    else:
        partEl.append(element)
    return partEl


def flattenAsString(element):
    """
    Converts array to a string, removes all brackets and duplicate commas, 
    splits the string back into list
    """
    newSt=str(element)
    newSt=newSt.replace(" ","")
    replacements = ["[","]","(",")"]
    for rep in replacements:
        newSt=newSt.replace(rep,",")
    #can do better with regex:
    while ",," in newSt:
        newSt=newSt.replace(",,",",")
    newSt=newSt.rsplit(",")
    newSt.pop(0)
    newSt.pop(-1)
    newList = [int(elem) for elem in newSt]
    return newList
