def conta_frases(frases):
    '''Conta quantas palavras tem em uma frase retirando: pontos finais, exclamações,
Interrogações e reticências'''
    lista = frases.replace('!','.').replace('?','.').replace('...','.')
    lista2 = lista.split('.')
    if (lista.endswith('.')):
        return len(lista2)-1
    else:
        return len(lista2)