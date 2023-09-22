def maiores (numeros: list[int], n: int)
'''dada uma lista de numeros inteiros retorna
outra lista que contenha todos os numeors da original
maiores que n, ordenados em ordem crescente'''
    for i in numeros:
        if i > n:
            return list(i)