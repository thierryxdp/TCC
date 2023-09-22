def posLetra(string,letra,n):
    """comentário"""
    i=0
    acum=[]
    while i<len(string):
        i+=1
        if string[i]==letra:
            acum+=[i]
    return acum[n]