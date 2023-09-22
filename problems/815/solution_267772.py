def insere(lista_numero, n):
    '''recebe uma lista ordenada e inclui n na posição correta'''
    if n not in lista_numero:
        a = lista_numero[:n] 
        b = list.index(lista_numero, n)
        c = list.count(n)
        return a + [n,] + lista_numero[a+b:]
        # lista_numero[(list.index(lista_numero, n) + list.count(n)):]
        
    else:
        x = list.index(lista_numero, n-1)
        y = list.index(lista_numero, n+1)
        return lista[:x] + [n,] + lista[y:]