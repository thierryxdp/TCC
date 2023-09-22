# Maiores
def maiores(lista,n):
    '''Essa função recebe uma lista de números e um outro número o qual ela deverá
    retornar em uma nova lista todos os números maiores que ele
    LIST, FLOAT -> LIST'''
    lista1 = lista[:]
    lista1.append(n)
    lista1.sort()
    return lista1[(lista1.index(n)+1):]


# Acima da Média
def acima_da_media(lista):
    '''Essa função recebe uma lista com as notas de uma turma e retorna uma nova lista
    ordenada apenas com as notas que ficaram acima da média das notas
    LIST -> LIST'''
    n = sum(lista)//len(lista)
    notas = maiores(lista,n)
    if n in notas:
        notas.remove(n)
    return notas