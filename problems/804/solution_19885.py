def filtra_pares(tupla):

    i = []
    
    if tupla[0] % 2 == 0:

        i.append(tupla[0])

        if tupla[1] % 2 == 0:

            i.append(tupla[1])

            if tupla[2] % 2 == 0:

                i.append(tupla[2])

                    if tupla[3] % 2 == 0:

                        i.append(tupla[3])
        

    return i