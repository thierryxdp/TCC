def maiores(listaNumeros, n):
    '''funçao que dada uma lista e um numero n, retorne uma outra lista'''
    '''list->list'''
    if n not in listaNumeros:
        listaNumeros.append(n)
        listaNumeros.sort()
        i = listaNumeros.index(n)
        sublista = listaNumero[i+1:]
        rep = sublista.count(n)
        return sublista[rep:]