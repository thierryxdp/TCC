def freq_palavras(frases):
    palavra = ''
    lista = []
    for termo in frases:
        if termo not in ' .,;!?':
            palavra = palavra + termo
        else:
            lista = lista + [palavra]
            palavra = ''
    return lista