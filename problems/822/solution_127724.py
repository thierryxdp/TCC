def repetidos(lista):
    i=0
    rep=0
    while i<(len(lista)-1):
        if lista[i]==(lista[i+1]):
            rep=1+rep
            i=i+1
        else:
            i=i+1
               
    return rep