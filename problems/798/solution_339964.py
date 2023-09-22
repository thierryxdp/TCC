def freq_palavras(frases):
    '''Recebe uma string contendo uma frase, e retorna um dicionário onde cada palavra
    da string passada se torna uma chave, e o valor será o número de vezes que a palavra
    aparece na frase.
    str -> dict'''
    lfrase = str.split(frases,' ')
    dicio = {}
    for palavra in lfrase:
        if palavra not in dicio:
            dicio[palavra] = 1
        else:
            dicio[palavra] = dicio[palavra] + 1
    return dicio