def filtraMultiplos(lista,n):
    termo = 0
    retorno = []
    while termo < len(lista):
        x = lista[termo]
        if x%n == 0:
            list.append(retorno,lista[termo])
        termo = termo + 1
    return retorno