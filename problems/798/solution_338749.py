def freq_palavras (frase):
    """ retorna o número de vezes que cada palavra aparece na frase de entrada. str -> dict"""
    frase2 = str.split(frase)
    listapa = []
    listanu = []
    for palavra in frase2:
        listapa += [palavra]
        listanu += [(str.count(frase2, palavra))]
    return dict(zip(listapa, listanu))