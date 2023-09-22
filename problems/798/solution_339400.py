def freq_palavras(x):
    '''Essa função serve para contar o número de vezes que uma palavra se repete
    em uma frase
    str->dict'''
    lista_palavras = x.split()
    dic = dict.fromkeys(lista_palavras,0)
    for i in range(len(lista_palavras)):
        dic[lista_palavras[i]] += 1
    return dic