def maiores(lista,n):
    '''
    Faça uma funçao que dada uma lista de numeros inteiros e um numero inteiro n
    Retorna outra lista contendo todos os numeros da lista original maiores que n, ordenados em ordem crescente
    '''
    N=[]
    for i in lista:
        if i > n:
            N.append(i)
    return sorted(N)