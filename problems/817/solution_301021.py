def maiores(lista,n):
    ''' Essa função recebe uma lista de números inteiros e um números inteiro n,
    e retorna outra lista que contém todos os números da primeira lista maiores
    que n e ordenados de forma crescente;
    list,int->list'''
    lista.append(n)
    list.sort(lista)
    x = list.index(lista,n)
    if n not in lista
    return lista[(x)+1:]

def acima_da_media(lista):
    ''' Essa função recebe uma lista com as notas de uma turma, e retorna
    uma lista ordenada com as notas que ficaram acima da média;
    list->list. '''
    l1 = sum(lista)
    l2 = len(lista)
    media = (l1/l2)
    resultado = maiores(lista,media)
    return resultado