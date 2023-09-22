def maiores(lista_numero,n):
    lista_numero.append(n)
    lista_numero.sort()
    if lista_numero > n:
        return lista_numero