def posLetra(string,letra,n):
    """
    Retorna em que posição da string a ocorrência da letra está.
    str, str, int -> int
    """
    posicao= string.find(letra)
    while h>= 0 and n>1:
        posicao= string.find(letra,posicao+1)
        n=n-1
    return posicao