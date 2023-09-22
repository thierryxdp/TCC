def numeros(lista, n):
    """função que dado uma lista contendo números inteiros, e um número inteiro (n), retorna outra lista contendo
    todos os números maiores que n
    list -> list"""

    maiores_numeros = list()
    for c in lista:
        if c > n:
            maiores_numeros.append(c)
    list.sort(maiores_numeros)

    return maiores_numeros

def acima_da_media(lista):
    """função que recebe uma lista com notas dos alunos, e retorna outra lista ordenada com as notas que ficaram
	acima da média
	list -> list"""
    
    media = sum(lista) / len(lista)
    
    return numeros(lista, media)