def filtra_pares(s):
    lista_pares=[]
    for elemen in s:
        if elemen %2==0:
            lista_pares.append(elemen)
            return lista_pares