def freq_palavras(frases):
    """ Função que recebe uma string e retorne um dicionário o qual cada palavra dessa string seja uma chave e tenha como valor o número de vezes que a palavra aparece;
    str -> dict"""
    dicionario = {}
    palavras = frases.split(" ")
    for palavra in palavras:
        if palavra in list(dicionario.keys()):
            dicionario[palavra] += 1
        else:
            dicionario[palavra] = 1
    return dicionario