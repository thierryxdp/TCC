def freq_palavras(frases):
    frase_separada = str.split(frases)
    i = 0
    resultado = {}
    while i < len(frase_separada):   
        dicionario = frase_separada[i]
        V = list.count(frase_separada, frase_separada[i])
        resultado[dicionario] = V
        i += 1
    return resultado