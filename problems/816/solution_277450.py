def maiores(lista, n):
    n = 1
    for elemento in lista:
        if elemento > n:
            list.sort(lista)
            lista_final.append(elemento)
            return[i for i in lista if i > n]