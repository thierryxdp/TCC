def freq_palavras(frases):
    dicionario={}
    frases=str.split(frases)
    for elem in range(len(frases)):
        qtd_vezes=list.count(frases,frases[elem])
        dicionario=dicionario+{frases[elem]:qtd_vezes}
    return dicionario