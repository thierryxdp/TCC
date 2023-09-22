def filtra_pares( tupla ):

    lista = ()

    for n in tupla:
        if tupla[0] % 2 == 0:
           x = tupla[0]
        if tupla[1] % 2 == 0:
           x = tupla[1]
        if tupla[2] % 2 == 0:
           x = tupla[2]
        if tupla[3] % 2 == 0:
           x = tupla[3]
            

    return x