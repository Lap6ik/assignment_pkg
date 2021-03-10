'''
__author__= Tatiana Lapshina, v1.1, 10/03/2021
This code below will flatten array(list or tuple) of numbers:
example: (1,18,(19,6,(100,32)))-->[1, 18, 19, 6, 100, 32]
final array will be a list 
'''
from threading import Thread

a = [[1,2,[3,8]],4,12,[72, 94, [11,12,[1,2,[18,[19,[1]]]]]]]
l = (1,18,(19,6,(100,32)))

b=[]
def flattenElement(element):
    if hasattr(element,'__len__') and not isinstance(element, str):
        for i in range(len(element)):
            thread=Thread(target=flattenElement, args=[element[i]])
            thread.start()
            thread.join()
    else:
        b.append(element)
        print (b)
    return b

flattenElement(l)
#flattenElement(a)
