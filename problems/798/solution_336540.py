def freq_palavras(frases):
    frase = frases.split(" ")
    dicionario = {}
    for palavras in frase:
        count = 1
        if palavra in dicionario:
            count = int(dicionario[palavra].split(" ")[-1] + 1
        dicionario[palavra] = palavra + : + str(count)
    for chave in dicionario:
        return dicionario[chave]