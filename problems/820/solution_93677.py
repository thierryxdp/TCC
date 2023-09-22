from random import randint
def posLetra(string,letra,num):
    i=0
    x=str.count(string,letra)
    if x!=num:
        return -1
    while i<len(string):
        y=str.find(string,letra)
    i=i+1
    return y