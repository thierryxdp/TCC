def insere(lista_numero, n):
    '''Retorna um dada lista (lista_numero) acrescendida do elmento (n) em ordem crescente
    list, int -> list'''
    lista_numero.append(n)
    list.sort(lista_numero)
    return lista_numero