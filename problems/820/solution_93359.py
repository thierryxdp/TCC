def posLetra(string,letra,n):
    """comentário"""
    i=0
    acum=[]
    while i<len(string):
        i+=1
        if string[i]==letra:
            acum+=[i]
    if len(acum)<n:
        return -1
    return acum[n]