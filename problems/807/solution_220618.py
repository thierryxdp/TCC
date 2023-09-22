def conta_frases(frases):
    '''Conta quantas palavras tem em uma frase retirando: pontos finais, exclamações,
Interrogações e reticências'''
    lista = frases.replace('!','.').replace('?','.').replace('...','.')
    lista2 = lista.split('.')
    return len(lista2)