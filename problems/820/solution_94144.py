def posLetra(texto,letra,numero):
    """dada uma string, uma letra e um número, a função retorna a posicão da
 ocorrência dada como entrada (número) da letra na string. Ex:
 >>>posLetra("mariana come banana","a",3) retorna 6.
 str, str, int-->int
 
 Parâmetros
 texto: frase dada como entrada
 letra: letra que será procurada e terá seu índice como retorno da função
 numero: numero da ocorrência da letra desejada"""
    n_repeticoes=str.count(texto,letra)
    if n_repeticoes<numero:
        return -1
    else:
        x=0
        y=0
        posicao=0
        while y<numero:
            posicao=str.index(texto,letra,x)
            x=posicao+1
            y=y+1
    return posicao