def freq_palavras(frase):
    texto = frase
    dicionario = {}
    for palavra in texto:
        if palavra in palavras_procuradas:
            count = 1
            if palavra in dicionario:
                count = int(dicionario[palavra].split(' ')[-1]) + 1;

    dicionario[palavra] = palavra + " " + str(count)
    for palavra in palavras_procuradas:
        if palavra not in texto:
            dicionario[palavra] = palavra + " " + str(0)
    return dicionario