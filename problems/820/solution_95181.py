def posLetra(string,letra,n):
    """ """
    i=0
    contagem=0
    if string.count(letra)>=n:
        while contagem !=n:
            if letra == string[i]:
                contagem+=1
            i+=1
        return i-1
           
    else:
        return -1