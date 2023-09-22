def filtra_pares(t):
    lista1= t
    lista = []   
    for t[0] in lista1 :
        if t[0] % 2 == 0:
            lista.append(t[0])
            for t[1] in lista1 :
                if t[1] % 2 == 0:
                    lista.append(t[1])
                    if t[2] % 2 == 0:
                        lista.append(t[2])