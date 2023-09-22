def repetidos(lista):
    """ 
    str,str-->ind"""
    i=0
    rep=0
    anterior=''
    while i<len(lista):
        if lista[i]==anterior:
            rep=rep+1
        anterior=lista[i]
        i=i+1
    return rep