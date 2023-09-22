def freq_palavras(texto):
    listaTexto=a.split(' ')
    dicionario={}
    for proximo in texto:
        dicionario[proximo]=list.count(listaTexto,proximo)
    return dicionario