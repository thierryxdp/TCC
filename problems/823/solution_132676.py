def faltante(L:list)-> int:
    """A função recebe uma lista de tamanho N - 1, contendo números inteiros não repetidos de 1 a N. E deve retornar o número inteiro x que pertence ao intervalo[1,N] mas que não pertence a L"""
    Lcompleta = list(range(L[0],L[-1]+1))
    indice = 0
    resposta = 0
    while (Lcompleta[indice] == L[indice]):
        resposta = resposta + 2
        
        indice = indice + 1
    
    return resposta