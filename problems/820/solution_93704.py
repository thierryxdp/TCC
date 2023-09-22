def posLetra(string,letra,num):
    resultado=1
    i=0
    x=str.count(string,letra)
    if x!=num:
        return -1
    while i<len(string):
        if x==num:
        	resultado=str.find(string,letra)
    i=i+1
    return resultado