def freq_palavras(frase):
    dici = {}
    frases = frase.split()
    for palavra in frases:
        if palavra in frases:
            soma = frases.count(palavra)
            dici[palavra] = soma
    return dici