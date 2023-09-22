def posLetra(string,letra,n):
    """
    Retorna a posição da string em que a ocorrência da letra está.
    str,str,int -> int
    """
    posicao=0
    ocorrencia=0
    while ocorrencia<n:
        if string[posicao]==letra:
            ocorrencia= ocorrencia+1
        posicao= posicao+1
    return posicao