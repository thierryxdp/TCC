def posLetra(string,letra,num):
    resultado=0
    i=0
    x=str.count(string,letra)
    while i<len(string):
        if x==1:
            resultado=str.index(string,letra)
        i=i+1
        if x<num:
            return -1
        if x>=num:
            y=str.replace(letra,'',x-1)
            resultado= str.index(string,letra)
    return resultado