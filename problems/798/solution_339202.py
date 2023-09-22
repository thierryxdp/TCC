def freq_palavras(frases):
    dicionario = {}
    for palavra in str.split(frases):
        n = list.count(palavra, frases)
        dicionario = dicionario + 'palavra':n
    return dicionario