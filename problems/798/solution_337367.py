def freq_palavras(frases):
    lista_frases = str.split(frases)
    dicionario_repeticao = {}
    for i in lista_frases:
        repete = list.count(lista_frases,i)
        dicionario_repeticao[i] = repete
    return dicionario_repeticao