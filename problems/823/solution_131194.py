def faltante(L):
    """Funcao que, dada uma lista L com N-1 inteiros numerados de 1 a N, descobre qual numero deste intervalo esta faltando;
    Entrada: list[int]
    Saida: int"""
    num = 1
    list.sort(L)
    
    if num not in L:
        return num
    
    elif len(L) in L:
        return len(L) + 1
    
    while num < len(L):
        if num not in L:
            return num
        num = num + 1