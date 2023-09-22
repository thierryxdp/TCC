def freq_palavras(frases):
    palavras=frases.split()
    dicionario={}
    contador=0
    for elemento in palavras:
        dicionario[palavras[contador]]=palavras.count(palavras[contador])
        contador+=1
    return dicionario