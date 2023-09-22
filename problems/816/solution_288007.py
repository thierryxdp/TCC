def maiores(lista,n):
    lista.sort(lista)
    lista_final = []
    for elemento in lista:
        if elemento > n:
            lista_final.append(elemento)
            return lista_final