def freq_palavras(frases):
    dicionario={}
    frases=str.split(frases)
    for elem in range(len(frases)):
        qtd_vezes=list.count(frases,frases[elem])
        if frases[elem] not in dicionario:
            dicionarios[frases[elem]]=qtd_vezes
    return dicionario