def soma_h(n):
    """ Dado um valor N, retorna o valor H com N termos"""
    soma = 0
    for numero in range(1,n+1):
        soma += 1/numero
    return round(soma,2)