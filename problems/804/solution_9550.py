def filtra_pares(tupla):
    ind0 = tupla[0]%2
    ind1 = tupla[1]%2
    ind2 = tupla[2]%2
    ind3 = tupla[3]%2
    tuplapares = ()
    if ind0 == 0:
        tuplapares = (tupla[0])
        if ind1 == 0:
            tuplapares = (tupla[0],tupla[1])
            if ind2 == 0:
                tuplapares = (tupla[0],tupla[1],tupla[2])
                if ind3 == 0:
                    tuplapares = (tupla[0],tupla[1],tupla[2],tupla[3])