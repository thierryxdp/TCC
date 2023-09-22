def freq_palavras(frases):
    frases=frases.split
    frase={}
    for i in range(len(frases)):
        qtd = frases.count(i)
        frase= frase+ qtd
    return frase