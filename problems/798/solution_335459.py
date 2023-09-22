def freq_palavras(frases):
    lista_frase = frases
    palavras_frase = lista_frase.split()
    conta_palavras= {}
    for palavra in palavras_frase:
        if palavra in conta_palavras:
            conta_palavras[palavra]= conta_palavras[palavra]+1
        else:
            conta_palavras.update({palavra:1})
    return conta_palavras