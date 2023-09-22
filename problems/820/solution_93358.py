def posLetra(string,letra,n):
    """comentário"""
    i=0
    acum=[]
    while i<len(string):
        i+=1
        if string[i]==letra:
            acum+=[i]
    if n<len(acum):
        return -1
     return acum[n]