def posLetra(string, letra, numero):
    '''funçao dada uma string, uma letra e um numero que indica a ocorrencia da letra retorna em que posiçao a ocorrencia da letra esta e se n tiver a ocorrencia retorna -1
    str, str, int -> int'''
    posicao = str.find(string, letra)
    while posicao >= 0 and numero > 1:
        posicao = str.find(string, letra, posicao + 1)
        numero -= 1
    return posicao