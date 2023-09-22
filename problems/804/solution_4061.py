def filtra_pares(tupla):
    
    lista = []

    for n in tupla:
        if n % 2 == 0:
            lista.insert(n)

    return lista