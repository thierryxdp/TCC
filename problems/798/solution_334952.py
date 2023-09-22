def freq_palavras(frases):
    ''''''
    dicionario = {}
    listapalavras = str.split(frases)
    for palavra in listapalavras:
        dicionario += {palavra:list.count(listapalavras,palavra)}
    return dicionario