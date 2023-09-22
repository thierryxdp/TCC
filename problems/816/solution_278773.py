def maiores(lista_inteiros,n):
    '''Função que recebe uma lista de números inteiros, um número inteiro n
        e retorna uma outra lista com todos os números da lista original que
        são maiores que n.'''
    list.insert(lista_inteiros,0,n)
    list.sort(lista_inteiros,reverse=True)
    y = list.index(lista_inteiros,n,0)
    del lista_inteiros[y::]