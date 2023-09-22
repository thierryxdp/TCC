from random import randint
def posLetra(string,letra,num):
    i=0
    x=str.count(string,letra)
    if x!=num:
        return -1
    while i<len(string):
        y=string[i]
    i=i+1
    return y