def repetidos(lista):
    i=0
    n=0
    while i<len(lista):
        if lista[i+1]==lista[i]:
        	n=n+1
        else:
            n=n
    i=i+1
    return n