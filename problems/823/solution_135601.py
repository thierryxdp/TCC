def faltante(L):
    """Função que, dada uma lista com N-1 inteiros, numerados de 1 a N, retorna o número inteiro desse intervalo que está faltando; lista->int"""
    
    indice = 0
    
    while indice < len(L):
        
        if L[0] != 1:
            return 1
        
        elif (L[indice] != L[indice+1]-1):
            return L[indice]+1
        
        elif (L[indice] == L[indice+1]-1):
            return L[-1]+1
        
        indice = indice+1