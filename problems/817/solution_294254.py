def maiores(lista_int,n):
    '''dada uma lista de números inteiros(lista_int) e um número inteiro(n), retorna outra lista,
    que contém todos os números da lista original maiores que n; list, int -> list '''
    lista = []
    lista_int.append(n)
    lista_int.sort()
    n1 = lista_int.index(n)
    lista = lista_int[n1+1:]
    return lista

def acima_da_media(l):
    '''dada uma lista com as notas dos alunos de uma turma(l), retorna uma lista ordenada com
    as notas que ficaram acima da da média; list -> list'''
    soma = sum(l)
    alunos = len(l)
    media = soma/alunos
    if media in l:
        l.remove(media)
    return maiores(l,media)