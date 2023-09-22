def faltante(lista):
    """Função que dado uma lista de números ela retorna o número faltante entre 1 a N. Dado de entrada é uma lista
    e na saída é um número inteiro"""
    N = max(lista)
    for numero in range(1,N):
        if numero not in lista:
            return numero
    return N+1