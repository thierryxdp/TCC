def faltante(lista):
    
    """Dada uma lista com numeros inteiros diferentes, retorna 
    os numeros pertencentes ao intervalo entre 1 e N. list -> int """
    posicao = 0
    while lista[posicao] < len(lista):
        if posicao+1 == lista[posicao]:
            posicao = posicao + 1
        
    return posicao+1