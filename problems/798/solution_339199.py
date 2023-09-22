def freq_palavras(frases):
    dicionario = {}
    for palavra in str.split(frases):
        n = count(palavra, frases)
        dicionario = dicionario + 'palavra':n
    return dicionario