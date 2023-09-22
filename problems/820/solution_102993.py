def posLetra(string,letra,n):
    '''função que dada uma string, uma letra e um número que
    indica a ocorrência desejada da letra, retorna em que 
    posição da string aquela ocorrência da letra está
    str,str,int -> int
    '''
    if n > str.count(string,letra):
        return -1
    posicao = string.find(letra)
    while posicao >= 0 and n > 1:
        posicao = string.find(letra,posicao + 1)
        n -= 1
    return posicao