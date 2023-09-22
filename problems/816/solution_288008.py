def maiores(lista,n):
    sorted(lista_numero, key=int)
    list.sort(lista_numero)
    lista_final = []
    for elemento in lista:
        if elemento > n:
            lista_final.append(elemento)
            return lista_final