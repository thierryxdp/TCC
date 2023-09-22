def maiores(L,n):
    '''Função que dado uma lista de números inteiros(L) e um número inteiro(n), retorna uma nova lista, que contenha todos os números da primeira lista maiores que n'''
    L.append(n)
    L.sort()
    index = L.index(n)
    return L[index+1:]