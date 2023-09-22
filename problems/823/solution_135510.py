def faltante(L):
    """Função que, dada uma lista com N-1 inteiros, numerados de 1 a N, retorna o número inteiro desse intervalo que está faltando; lista->int"""
    
    contador = -1
    indice = 0
    
    while contador < len(L):
        if(L[indice]+1 != L[indice+1]):
            return L[indice]+1
        contador = contador+1