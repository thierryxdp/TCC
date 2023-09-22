def freq_palavras(frases):
    palavras = str.split(frases)
    dicionario = {}
    for palavra in palavras:
        dicionario = {palavra: str.count(palavra,frases)}