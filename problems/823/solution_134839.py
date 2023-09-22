def faltante (listaL):
    """Função que recebe uma lista de tamanho N-1 contenco números inteiros e retorna o número inteiro x que pertence ao intervalo [1,N], mas não pertence a lista de entrada
    entrada: list
    saída: int"""
    i=0
    peca=1
    while i<len(listaL)+1:
        if peca in listaL:
            peca=peca+1
            i=i+1
        else:
            return peca