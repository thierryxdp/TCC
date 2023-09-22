def insere(lista_numero, n):
    '''recebe uma lista ordenada e inclui n na posição correta'''
    if n in lista_numero:
        a = lista_numero[:n] 
        b = list.index(lista_numero, n)
        c = list.count(n)
        return a + [n,] + lista_numero[a+b:] 
    else:
        d = n-1
        e = n+1
        x = list.index(lista_numero, d)
        y = list.index(lista_numero, e)
        return lista[:x] + [n,] + lista[y:]