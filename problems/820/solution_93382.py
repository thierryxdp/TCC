def posLetra(string,letra,n):
    """comentário"""
    i=0
    acumulador=[]
    while i<len(string):
        if string[i]==letra:
            acumulador+=[i]
        i+=1
    if len(acumulador)<n:
        return -1
    else:
        return acumulador[n-1]