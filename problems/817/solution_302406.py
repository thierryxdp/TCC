def maiores(li,n):
    '''Dada uma lista li de números inteiros e um número inteiro n, retorna outra
    lista, que contenha todos os números da lista original maiores que n ordenados em ordem crescente
    list, int --> list'''
    lista = li + [n]
    list.sort(lista)
    qts_n = list.count(lista,n)
    indice = list.index(lista,n)+ qts_n
    return lista[indice:]


def acima_da_media(li):
    '''Dada uma lista com as notas dos alunos de uma turma, retorna
    uma lista ordenada com as notas que ficaram acima da média.
    list, int --> list'''
    media = (sum(li))/(len(li))
    return maiores(li,media)