def freq_palavras (frase):
    """ retorna o número de vezes que cada palavra aparece na frase de entrada. str -> dict"""
    f = str.split(frase)
    dic = {}
    for palavra in f:
        dic1 = {palavra : str.count(frase, palavra)} in dic
    return dic1