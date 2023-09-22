def maiores(lista,n):
    '''funcao que retorna uma lista que contém todos os números maiores que n'''
    if n not in lista:
        lista.append(n)
    lista.sort()
    x = lista.index(n)
    lista2 = lista[x+1:]
    y = lista2.count(n)
    return lista2[y:]