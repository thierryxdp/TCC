def maiores(lista, n):
    n = 1
    lista_final = []
    for elemento in lista:
        if elemento > n:
            list.sort(lista)
            list.sort(n)
            lista_final.append(elemento)
            return[i for i in lista if i > n ]