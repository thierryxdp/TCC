from random import randint
def posLetra(string,letra,num):
    resultado=1
    i=0
    x=str.count(string,letra)
    while i<len(string):
        if resultado==1:
        	return -1
        if resultado>1:
        	y=str.find(string,letra)
    i=i+1
    return resultado