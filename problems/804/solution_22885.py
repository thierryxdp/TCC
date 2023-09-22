def filtra_pares (tupla):
    lis_final = list()
    for x in tupla:
        if x % 2 == 0:
            list_final += [x]
            
            tuple_final = tuple(list_final)
            return tuple_final