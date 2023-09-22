def repetidos(lista):
    rep = 0
    for n in range(len(lista)):
        if(lista[n]==lista[n+1]):
            rep += 1 
            for elem in range(len(lista)):
                if(lista[elem]==lista[elem+1]):
                    rep += 1
                    else:
                        return rep+1