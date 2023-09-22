def posLetra(texto, letra, n):
    '''função que recebe como entrada uma string,uma letra e um número que indica a ocorrência desejada da letra e retorna em que posição da string aquela ocorrência da letra está; str, str, int -> int'''
    posicao = str.find(texto,letra)
    while posicao >= 0 and n > 1:
        posicao = str.find(texto,letra, posicao + 1)
        n -= 1
    return posicao