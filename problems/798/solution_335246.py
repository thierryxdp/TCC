def freq_palavras(frases):
    dicionario = {'chave':'valor'}
    diminuir = str.split(frases, ' ')
    for corredor in range(len(diminuir)):
        dicionario[diminuir[corredor]] = list.count(diminuir, diminuir[corredor])        
    del(diminuir)['chave']
    return diminuir