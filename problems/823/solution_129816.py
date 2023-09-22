def faltante (lista):
    """Função que, dada uma lista de tamanho N - 1 contendo números inteiros de 1 a N, retorna o número inteiro que pertence ao intervalo [1,N], mas que não pertence a lista de entrada
    entrada: list
    saída: int"""
    
    N = max(lista)
    lista_comp = list(range(1,N+1))
    proximo = 0
    
    while proximo < len(lista):        
        if lista_comp[proximo] in lista:
            proximo = proximo + 1
            
        if lista_comp == lista:
            return N+1
            
        if lista_comp[proximo] not in lista:
            return lista_comp[proximo]