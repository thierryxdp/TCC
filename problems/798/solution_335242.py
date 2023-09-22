def freq_palavras(frases):
    dicionario = {'chave':'valor'}
    diminuir = str.split(frases, ' ')
    for corredor in diminuir:
        diminuir[dicionario[corredor]] = list.count(diminuir, diminuir[corredor])        
        del(diminuir)['chave']
    return diminuir