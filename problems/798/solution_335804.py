def freq_palavras(frases):
    dicionario=()
    palavras=frases.split()
    for coisa in palavras:
        if palavras.count(coisa)>0:
            dicionario=dicionario+coisa+palavras.count(coisa)
        return dicionario