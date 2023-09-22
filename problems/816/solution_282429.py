def maiores (lista, n)
'''dada uma lista de numeros inteiros retorna
outra lista que contenha todos os numeors da original
maiores que n, ordenados em ordem crescente
list, int -> list'''
    a=([i for i in lista if i > n])
    return sorted(a)