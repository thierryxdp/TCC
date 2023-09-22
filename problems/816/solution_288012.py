def maiores(lista,n):
    sorted(lista, key=int)
    list.sort(lista)
    lista_final = []
    for elemento in lista:
        if elemento > n:
            lista_final.insert(elemento)
            return lista_final