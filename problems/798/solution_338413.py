def pal(string):
    """ verifica quantas ocorrencias tem de cada palavra
    na frase str-> dic """
    palavras = string.split(" ")
    ocorrencias = {}
    for palavra in palavras:
        if palavra in ocorrencias :
            ocorrencias[palavra] = ocorrencias[palavra] + 1
        else:
            ocorrencias.update({palavra:1})
    return ocorrencias