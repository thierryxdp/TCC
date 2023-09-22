def maiores(lista,n):
    '''função que dada uma lista de números e determinado
    número inteiro n como entradas, retorna outra lista
    contendo os números da lista original maiores que n,
    ordenados do menor para o maior
    string -> string'''
    maiores_numeros=list()
    for c in lista:
        if c >= n:
            maiores_numeros.append(c)
    return maiores_numeros

	valores = list(map(int, input().split()))
	num = int(input())