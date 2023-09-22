def maiores(lista,n):
    '''Função que dada uma lista de numeros inteiros e um numero inteiro n
    retorna outra lista que contenha todos os numeros da lista original maiores q n'''
    list.append(lista,n)
    list.sort(lista)
    posicao=list.index(lista,n)
    return lista[posicao+1:]