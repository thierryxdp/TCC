def freq_palavras(string):
    lista = str.split(string)
    dicionario = {}
    for n in lista:
        dicionario[n] = str.count(string, n)
        while n in lista:
            list.remove(lista, n)
    return dicionario