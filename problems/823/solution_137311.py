def faltante(L):
    """Recebe uma lista L com os números de um quebra-cabeça e diz qual a peça que está faltando;
    	list -> int"""
    list.sort(L)
    indice=0
    N=len(L)-1
    while indice<=N:
        if L[indice]!=(L[indice]+1):
            pecafaltante=(L[indice]-1)
        indice=indice+1
    return pecafaltante