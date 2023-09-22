def freq_palavras(frases):
    
    dicionario = {}
    lista = str.split(frases)
    for palavra in lista:
        dicionario[palavra] = list.count(frases)
    return dicionario