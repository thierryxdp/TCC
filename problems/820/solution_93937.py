def posLetra(string,letra,num):
    resultado=0
    i=0
    x=str.count(string,letra)
    if x!=num:
        return -1
    while i<len(string):
        if x==1:
            resultado=str.index(string,letra)
        i=i+1
    return resultado