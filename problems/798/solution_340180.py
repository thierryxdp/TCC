def freq_palavras(frases):
    """Determinar um dicionario com os indices como as palabras da frase e os valores sendo as ocorrências das mesmas;
    str -> dict"""
    dicionario = {}
    palavras = frases.split(" ")
    for palavra in palavras:
        if palavra in list(dicionario.keys()):
            dicionario[palavra] += 1
        else:
            dicionario[palavra] = 1
    return dicionario