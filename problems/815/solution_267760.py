def insere(lista_numero, n):
    '''recebe uma lista ordenada e inclui n na posição correta'''
    if n not in lista_numero:
        return lista_numero[:n] + [n,] + [lista_numero.index(n) + lista_numero.count(n):]
    else:
        x = lista_numero.index(n-1)
        y = lista_numero.index(n+1)
        return lista[:x] + [n,] + lista[y:]