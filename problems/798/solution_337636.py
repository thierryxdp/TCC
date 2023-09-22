def  freq_palavras(frases):
    lista = frases.split()
    dict1 = dict()
    i = 0
    while i < len(lista):
        dict1[lista[i]] = str.count(lista, lista[i])
        i += 1
    return dict1