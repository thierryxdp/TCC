def posLetra(string,letra,n):
    '''Retorna a posição da n-ésima ocorrência da letra dada na string inserida; str, str, int -> int'''
    indice=0
    posicao=0
    if str.count(string, letra)<n:
        return -1
    while posicao<n:
        if string[indice]==letra:
            posicao=posicao+1
        indice=indice+1
    return indice-1