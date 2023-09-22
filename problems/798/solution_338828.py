def freq_palavras(frase):
    dici = {}
    lista = str.split(frase)
    for i in range(len(lista)):
        if lista[i] in dici:
            dici[lista[i]] += 1
        else:
            dici[lista[i]] = 0
    return dici