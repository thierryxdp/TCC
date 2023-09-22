def maiores(lista,n):
    lista_maiores = list()
    inserir = lista.append(n)
    ordenar = lista.sort()
    i = lista.index(n)
    if n in ordenar:
        return ordenar[i+1:]