def freq_palavras (frase):
    """ retorna o número de vezes que cada palavra aparece na frase de entrada. str -> dict"""
    f = str.split(frase)
    listapa = []
    listanu = []
    for palavra in f:
        listapa += [palavra]
        listanu += [str.count(f, palavra)]
    return dict(zip(listapa, listanu))