def faltante (lista):
    """Função que, dada uma lista de tamanho N - 1 contendo números inteiros de 1 a N, retorna o número inteiro que pertence ao intervalo [1,N], mas que não pertence a lista de entrada
    entrada: list
    saída: int"""
    
    N = max(lista)
    lista2 = list(range(N+1))
    proximo = 0
    
    while proximo <= len(lista):
        if lista2[proximo] in lista:
            proximo = proximo + 1
            
        if lista2[proximo] not in lista:
            return lista2[proximo]