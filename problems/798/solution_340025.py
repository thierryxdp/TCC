def freq_palavras(frase):
    dicio = {}
    lista_frase = str.split(frase,' ')
    for i in lista_frase:
        if i not in dict.keys(dicio):
            dicio[i] = list.count(lista_frase,i)
    return dicio