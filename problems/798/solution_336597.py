def freq_palavras(x):
    lista_palavras = x.split()
    dic = dict.fromkeys(lista_palavras,0)
    for i in range(len(lista_palavras)):
        dic[lista_palavras[i]] += 1
    return dic