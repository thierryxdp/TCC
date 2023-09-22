def maiores(lista,n):
    '''
    Dado uma lista de numeros inteiros e um numero inteiro n, 
    ordena em crescente os números maiores que n.

    Uso:
    maiores(lista,n)

    Entrada:
    - lista (list, int): Lista original
    - n  (int): Número inteiro

    Saída:
    - Retorna uma nova lista que contem todos os numeros da lista
    original maiores que n, ordenados em ordem crescente. (lista, int)
    '''
    
    a=([i for i in lista if i > n])
    return sorted(a)