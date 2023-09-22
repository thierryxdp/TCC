def maiores(lista1,n):
    '''função que, dados uma lista de números inteiros
    e um número inteiro n, retorna outra lista, que contém
    todos os números da lista original maiores que n, 
    ordenados em ordem crescente
    list, int -> list'''
    x = 0
    y = len(lista1)
    lista2 = []
    while x != y:
        if lista1[x] > n:
            list.append(lista2,lista1[x])
        x = x + 1
    list.sort(lista2)
    return lista2

def acima_da_media(notas):
    '''função que, dad auma lista com as notas dos alunos
    de uma turma, retorna uma lista ordenada com as notas 
    que ficaram acima da média
    list -> list'''
    media = sum(notas)/len(notas)
    lista = maiores(notas,media)
    return lista