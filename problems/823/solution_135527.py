def faltante(L):
    """Função que, dada uma lista com N-1 inteiros, numerados de 1 a N, retorna o número inteiro desse intervalo que está faltando; lista->int"""
    
    indice = 0
    peca = 0
    
    while indice < len(L)+3:
        
        if L[indice]+1 != L[indice+1]:
            
            peca = peca+L[indice+1]-1
            
        indice = indice+1
    return peca