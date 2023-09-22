def freq_palavras(frases):
    """ verifica quantas ocorrencias tem de cada palavra
    na frase str-> dic """
    palavras = frases.split(" ")
    ocorrencias = {}
    for palavra in palavras:
        if palavra in ocorrencias :
            ocorrencias[palavra] = ocorrencias[palavra] + 1
        else:
            ocorrencias.update({palavra:1})
    return ocorrencias