def freq_palavras(frases):
    palavra = ''
    lista = []
    for termo in frases:
        if termo != ' ':
            palavra = palavra + termo
            else:
            lista = lista + [palavra]
            palavra = ''
    return lista