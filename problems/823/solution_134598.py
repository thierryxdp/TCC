def faltante(listaL):
    """funcao que dada uma lista de tamanho N-1 com inteiros numerados de 1 a N, retorna o numero que falta no intervalo;
       list->int"""
    i=1
    peca=0
    N=len(listaL)+1
    while i<N:
        if i not in listaL:
            peca=peca+i
        else:
            peca=i+1
        i=i+1
    return peca