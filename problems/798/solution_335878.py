def freq_palavras(texto):
    listaTexto=texto.split(' ')
    dicionario={}
    for proximo in texto:
        dicionario[proximo]=list.count(listaTexto,proximo)
    return dicionario