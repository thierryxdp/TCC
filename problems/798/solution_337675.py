def freq_palavras(frase):
    '''função que diz o número de vezes que uma palavra se repete numa frase'''
    d = {}
    s = str.split(frase)
    for palavra in s:
        if palavra in d:
            d[palavra] = d[palavra] + 1
        else:
            d[palavra] = 1
    return d