def repetidos(lista):
    rep = 0
    for n in range(len(lista)):
        for m in range(len(lista)):
            if(lista[n][m]==lista[n+1][m+1]):
                rep = +1
            else:
                return rep+1