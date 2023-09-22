def repetidos(lista):
    rep = 0
    for n in range(0,len(lista)):
        if(lista[n]==lista[n+1]):
            rep += 1
        else:
            return rep