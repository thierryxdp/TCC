def freq_palavras (frase):
    """ retorna o númeor de vezes que cada palavra aparece na frase de entrada. str -> dict"""
    f = str.spli(frase)
    dic = {}
    for palavra in f:
        dic = {palavra : str.count(palavra)} + dic
    return dic