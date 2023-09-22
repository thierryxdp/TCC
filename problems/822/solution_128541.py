def repetidos(lista):
    rep = 0
    for n in range(len(lista)):
        for m in range(len(lista)):
            if(lista[n]==lista[n+1]):
            elif(lista[m]==lista[m+1]):
                rep = +1
            else:
                return rep+1