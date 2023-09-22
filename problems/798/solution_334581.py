def freq_palavras(frases):
    palavra = ''
    lista = []
    for termo in frases:
        if termo != ' ':
            palavra = palavra + termo
        if termo == ' ':
            lista = lista + [palavra]
    return lista