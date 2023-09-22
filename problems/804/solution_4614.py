def filtra_pares(*tuple_):
    k = [] #Declarando lista
    for i in tuple_: 
        for j in i:
            if int(j) % 2 == 0: #Se o iésimo elemento é par, o adicionamos à lista.
                k.append(j)
    return tuple(k) #Retornamos a tuple.