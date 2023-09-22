def faltante(lista_L:list) -> int:
    """Essa função, dada uma lista L de tamanho N contendo números inteiros
    de 1 a N, retorna o número inteiro x que pertence ao intervalo [1,N], 
    mas que não pertence a lista de entrada L"""
    i = 0
    N = lista_L[-1]
    n = 0
    lista_dois = list(range(1,N+1))
    while i < len(lista_dois):
        if lista_dois[i] not in lista_L:
            n = n+lista_dois[i]
        i+=1
    if n == 0:
        n = len(lista_dois)+1
    
    return n