def filtra_pares(tupla):

    i = []
    
    if tupla[0] % 2 == 0:

        i.append(tupla[0])

    elif tupla[1] % 2 == 0:

            i.append(tupla[1])

    elif tupla[2] % 2 == 0:

                i.append(tupla[2])

    elif tupla[3] % 2 == 0:

                    i.append(tupla[3])      

    i = tuple(i)
    return i