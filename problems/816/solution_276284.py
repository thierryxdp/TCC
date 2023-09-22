# Maiores
def maiores(lista,n):
    '''Essa função recebe uma lista de números e um outro número o qual ela deverá
    retornar em uma nova lista todos os números maiores que ele
    LIST, FLOAT -> LIST'''
    lista1 = lista[:]
    lista1.append(n)
    lista1.sort()
    return lista1[(lista1.index(n)+1):]