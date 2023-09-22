def freq_palavras(frases):
    '''Função que retorna um dicionário com as strings dada na entrada
    e a quantidade de vezes que elas aparecem
    str -> dict'''
    dicionario = {}
    palavras = str.split(frases)
    for palavra in palavras:
        if palavra not in dicionario:
            dicionario[palavra] = 1
        else:
            dicionario[palavra] = dicionario.get(paalvra)+1
    return dicionario