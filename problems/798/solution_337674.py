def freq_palavras(frase):
    '''função que diz em que posição a palavra está dentro de uma frase'''
    d = {}
    s = str.split(frase)
    for palavra in s:
        if palavra in d:
            d[palavra] = d[palavra] + 1
        else:
            d[palavra] = 1
    return d