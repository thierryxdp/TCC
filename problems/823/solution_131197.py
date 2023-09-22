def faltante(L):
    """Funcao que, dada uma lista L com N-1 inteiros numerados de 1 a N, descobre qual numero deste intervalo esta faltando;
    Entrada: list[int]
    Saida: int"""
    num = 2
    list.sort(L)
    
  
    
    while num <= len(L):
        if num not in L:
            return num
        num = num + 1
  	if 1 not in L:
        return 1
    
    elif len(L) in L:
        return len(L) + 1