def acima(lista, n):
    '''Função que dada uma lista de números inteiros e um número inteiro n, retorna outra
lista, que contenha todos os números da lista original maiores que n ordenados em ordem crescente;
       list, int --> list'''
    lista2 = [x for x in lista if x > n]
    lista2.sort()
    return lista2

def acima_da_media(lista_notas):
    '''Função que dada uma lista com as notas dos alunos de uma turma,
    retorna uma lista ordenada com as notas que ficaram acima da média;
    list --> list'''
    media = (sum(lista_notas))/len(lista_notas)
    return acima(lista_notas, media)