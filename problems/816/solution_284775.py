def maiores (lista, n):
    '''numeros da lista original maiores que n'''
    list(lista)
    lista.append(n)
    listaOrg = sorted(lista)
    i = listaOrg.index(n)
    if n in listaOrg:
        lista.append(n)
    return listaOrg[i+1]