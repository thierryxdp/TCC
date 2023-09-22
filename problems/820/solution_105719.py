def posLetra(string, letra, n):
    """função que dada uma string, uma letra e um número indica a ocorrência desejada da letra.
    str, str, int -> int"""
    posicao = string.find(letra)
    while posicao >= 0 and n > 1:
        posicao = string.find(letra, posicao + 1)
        n -= 1
    return posicao