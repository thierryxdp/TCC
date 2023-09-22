def maiores (numeros: List[int], n: int):
        'Função que dada uma lista com números inteiros e um numero inteiro n, retorna os numeros maiores que n em ordem crescente
    for i in numeros:
        if i > n:
            return list(i)