def posLetra(string,letra,n):
    '''Esta e a funcao que recebe como entrada uma string,
    uma letra e um numero que indica a ocorrencia desejada
    da letra e retorna em que posicao da string a ocorrencia
    da letra esta'''
    pos = string.find(letra)
    while pos >= 0 and n > 1:
        pos = string.find(letra, pos + 1)
        n -= 1
    return pos