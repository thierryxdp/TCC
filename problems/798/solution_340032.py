def freq_palavras(frases):
    """ Função que recebe uma string e retorne um dicionário o qual cada palavra dessa string seja uma chave e tenha como valor o número de vezes que ;
    str -> dict"""
    dicio = {}
    palavras = frases.split(" ")
    for palavra in palavras:
        if palavra in list(dicio.keys()):
            dicio[palavra] += 1
        else:
            dicio[palavra] = 1
    return dicio