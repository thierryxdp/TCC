def faltante(L):
    """Funcao que, dada uma lista L com N-1 inteiros numerados de 1 a N, descobre qual numero deste intervalo esta faltando;
    Entrada: list[int]
    Saida: int"""
    
    indice=0
    x=0
    while indice < len(L):
        if L[indice]!=(indice+1):
            x=indice+1
        indice=indice+1
    return x