def maiores(m,n):
    '''
    Função que dada uma lista de números inteiros e um número inteiro n, retorna
    outra lista, contendo todos os números da lista original maiores que n, ordenados
    em ordem crescente)
    list, int-> list
    '''
    list.insert(m,n-1,n)
    list.remove(m,m<n)
    list.reverse(m)
    return m