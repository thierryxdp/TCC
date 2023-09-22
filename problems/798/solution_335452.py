def freq_palavras(frases):
    lista_frase = frases
    palavras_frase = lista_frase.split()
    conta_palavras= {}
    for palavra in range(len(palavras_frase)):
        if palavras in conta_palavras:
            conta_palavras[palavra]= conta_palavras[palavra]+1
    return conta_palavras