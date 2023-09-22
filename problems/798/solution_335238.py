def freq_palavras(frases):
    dicionario = {'chave':'valor'}
    diminuir = str.split(frases, ' ')
    for corredor in diminuir:
        dicionario[diminuir[corredor]] = list.count(diminuir, diminuir[i])        
        del(diminuir)['chave']
    return diminuir