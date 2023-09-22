def repetidos(lista):
    rep=0
    i=0
    while i<len(lista):
    	lista[i+1:]
        if lista[i]<lista[i+1]:
            rep=rep+1
            i=1+i
        else:
            i=1+i
    return rep