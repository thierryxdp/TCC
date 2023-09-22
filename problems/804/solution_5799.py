def filtra_pares(s):
    lista_pares=[]
    for n in s:
        if n %2==0:
            lista_pares.append(n)
            return lista_pares