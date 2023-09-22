def maiores(lista_numero,n):
    lista_numero.append(n)
    lista_numero.sort()
    posicao = lista_numero.index(n)
    return lista_numero[posicao+1:]