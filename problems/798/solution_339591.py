def freq_palavras(frase):
    '''Retorna um dicionário onde as palavras são chaves e a quantidade que cada uma
    aparece na frase é o valor que elas referenciam.
    str -> dict'''

    palavras = str.split(frase)
    dicionario = {}

    for palavra in palavras:
        if palavra not in dicionario:
            dict.update(dicionario,{palavra:1})
        else:
            dicionario[palavra] = dicionario[palavra] + 1

    return dicionario