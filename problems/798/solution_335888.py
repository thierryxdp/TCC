def freq_palavras(frases):
    palavras=frases.split()
    dicionario={}
    indice=0
    for palavra in palavras:
        dicionario[palavras[indice]] = palavras.count(palavras[indice])
    indice= indice + 1
    return dicionario