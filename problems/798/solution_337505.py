def freq_palavras(frases):
    '''
    Para esse função foi separado todas as palavras,
    contabilizada, quantas vezes cada palavra está na frase.
    '''
    # str-> str -> dict
    separado = str.split(frases)
    i = 0
    D = {}
    while i < len(separado):
        
        dicio = separado[i]
        V = list.count(separado, separado[i])
        D[dicio] = V
        i+=1
    return D