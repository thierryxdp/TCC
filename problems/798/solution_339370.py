def freq_palavras(frases):
    '''Recebe uma string e retorna um dicionário cujas chaves são as palavras da string e cujos valores são o número de vezes que cada palavra aparece na string;
    str -> dict'''
    dict = {}
    c = Counter()
    for palavra in frases:
        c[palavra] = c[palavra] + 1
    return c[palavra]