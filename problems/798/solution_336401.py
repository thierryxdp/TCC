def freq_palavras(string):
    lista = str.split(string)
    dicionario = {}
    for n in lista:
        dicionario[n] = str.find(string, n)
    return dicionario