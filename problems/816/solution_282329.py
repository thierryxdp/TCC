def maiores(listainteiros,n):
    '''Função que recebe uma lista de números inteiros, um número inteiro n
        e retorna uma outra lista com todos os números da lista original que
        são maiores que n.'''
    list.insert(listainteiros,0,n)
    list.sort(listainteiros,reverse=True)
    x = list.index(listainteiros,n,0)
    del listainteiros[x::]
    

    return listainteiros[::-1]