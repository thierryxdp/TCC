def maiores(lista,n):
    '''Função que dada uma lista de números inteiros e um
    número inteiro(n), retorna outra lista que contém todos 
    os números maiores que n.
    list -> list'''
    
    if n not in lista:
        lista.append(n)
    lista.sort()
    x = lista.index(n)
    lista2 = lista[x+1:]
    y = lista2.count(n)
    return lista2[y:]