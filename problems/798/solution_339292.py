def freq_palavras(frases):
    dicionario={}
    palavras=str.split(frases)
    vezes=0
    for palavra in palavras:
        vezes=str.count(frases,' '+palavra+' ')
        dicionario[palavra] = vezes
    return dicionario