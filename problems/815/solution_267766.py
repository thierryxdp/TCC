def insere(lista_numero, n):
    '''recebe uma lista ordenada e inclui n na posição correta'''
    if n not in lista_numero:
        return lista_numero[:n] + [n,] + [list.index(lista_numero, n) + list.count(n):]
    else:
        x = list.index(lista_numero, n-1)
        y = list.index(lista_numero, n+1)
        return lista[:x] + [n,] + lista[y:]