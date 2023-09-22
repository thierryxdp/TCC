def maiores(lista,n):
    '''Dados uma lista de números inteiros e um número
    inteiro n, retorna outra lista, que contenha todos os
    números da lista original maiores ou iguais a n, 
    ordenados em ordem crescente.
    list, int -> list'''
    if n in lista:
        list.sort(lista)
        inicio=list.index(lista,n)
        return lista[inicio:]
    else:
        list.append(lista,n)
        list.sort(lista)
        inicio=list.index(lista,n)
        return lista[inicio+1:]

def acima_da_media(lista_notas):
    '''Dada uma lista com as notas dos alunos de uma turma,
    retorna uma lista ordenada com as notas que ficaram
    acima da média.
    list -> list'''
    return maiores(lista_notas,5)