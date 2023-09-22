def freq_palavras(frase):
    texto = str.split(frase)
    dicionario = {}
    for i in texto:
        if i in frase:
            dicionario += 1