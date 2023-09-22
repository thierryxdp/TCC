def maiores(lista,n):
    '''
    função que dada uma lista de números inteiros e um inteiro n, retorna outra lista que contenha todos os números da lista original maiores que n ordenados em ordem crescente;
    lista, int -> list
    '''
    lista[0:0] = [n]
    list.sort(lista)
    indice = list.index(lista,n)
    del lista[:indice]
    list.sort(lista)
    del lista[0]
    return lista

def acima_da_media(lista):
    '''
    função que dada uma lista com as notas de toda a turma, retorna uma lista ordenada com as notas que ficaram acima da média adotada como 5;
    list -list
    '''
    media = sum(lista)/len(lista)
    return maiores(lista,media)