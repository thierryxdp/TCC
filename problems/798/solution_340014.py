freq_palavras(frase):
    dicio = {}
    lista_frase = str.plit(frase,' ')
    for i in lista_frase:
        if i not in dict.keys(dicio):
            dicio[i] = str.count(frase,i)
    return dicio