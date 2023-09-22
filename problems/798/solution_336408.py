def freq_palavras(string):
    lista = str.split(string)
    dicionario = {}
    for n in lista:
        dicionario[n] = list.count(lista, n)
    return dicionario