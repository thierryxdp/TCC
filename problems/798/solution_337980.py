def freq_palavras(frases):
    '''numero de vezes que a palavra aparece na frase'''
    lista = str.split(frases, ' ')
    dicio = {}
    for x in lista:
        dicio[x] = list.count(lista,x)
    return dicio