def freq_palavras (frase):
    """ retorna o númeor de vezes que cada palavra aparece na frase de entrada. str -> dict"""
    f = str.split(frase)
    dic = {}
    for palavra in f:
        dic = {palavra : str.count(frase, palavra)}
    return dic