def maiores (lista,n):
    '''Insita uma lista de numeros e um numero inteiro para que a função retorne outra lista que contenha os numeros da lista inserida, maiores que o n, ordenados em ordem crescente'''
    '''str, int -> str'''
    maiores = list()
    lista.sort()
    for ordem in lista:
        if ordem >= n:
            maiores.append(ordem)
            return maiores