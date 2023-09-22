def insere(lista_numero, n):
    '''recebe uma lista ordenada e inclui n na posição correta'''
    if n in lista_numero:
        a = lista_numero[:n] 
        b = list.index(lista_numero, n)
        c = list.count(n)
        return a + [n,] + lista_numero[a+b:] 
    else:
        lista2 = lista_numero[:n] + [n,] + lista_numero[n:]
        return list.sort(lista2)