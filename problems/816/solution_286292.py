def maiores(lista_numero, n):
    if n in lista_numero:
        posicao_n = list.index(lista_numero, n)
        del lista_numero[posicao_n:0]
        return lista_numero
    else:
        return False