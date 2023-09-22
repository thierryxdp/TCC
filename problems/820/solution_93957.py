def posLetra(string,letra,num):
    resultado=0
    i=0
    x=str.count(string,letra)
    while i<len(string):
        if x==1:
            resultado=str.index(string,letra)
        if x<num:
            return -1
        if x>=num and x!=1:
            pos=x-1
            y=str.replace(string,letra,' ',pos)
            resultado= str.index(y,letra)
        i=i+1
    return resultado