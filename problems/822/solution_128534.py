def repetidos(lista):
    rep = 0
    for n in range(-1,len(lista)+1):
        if(lista[n]==lista[n+1]):
            rep += 1 
        else:
            return rep+1