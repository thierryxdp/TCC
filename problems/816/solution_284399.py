def maiores(lista,n):
    '''Esta e a funcao que dada uma lista de numeros inteiros
    e um numero inteiro n, retorna outra lista que contenha
    todos os numeros da lista original maiores do que n
    ordenados em ordem crescente'''
    l2 = []
    for numeros in n:
        if numeros > n:
            l2.append(numeros)
            l2.sort(numeros)
            return l2