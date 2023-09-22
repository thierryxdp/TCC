def maiores(lista,n):
    '''Função que dada uma lista com números inteiros e um
    número inteiro n retorne uma outra lista, dessa vez com 
    apenas os números maiores que n da lista original
    list, int --> list.'''
    maiores_n = list()
    for a in lista:
        if a < n:
            maiores_n.append(a)
            return maiores_numeros