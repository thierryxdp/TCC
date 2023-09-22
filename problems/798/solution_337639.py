def  freq_palavras(frases):
    '''conta quantas vezes uma palavra se repete na frase
    str -> dict'''
    lista = frases.split()
    dict1 = dict()
    i = 0
    while i < len(lista):
        dict1[lista[i]] = list.count(lista, lista[i])
        i += 1
    return dict1