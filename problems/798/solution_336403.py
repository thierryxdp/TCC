def freq_palavras(string):
    lista = str.split(string)
    dicionario = {}
    for n in lista:
        dicionario[n] = str.count(string, n)
        list.remove(lista, n)
    return dicionario