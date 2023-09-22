def lingua_p(palavra):
    '''Funcao que traduz a palavra inserida para
    lingua do P.
    str -> str
    '''
    lista = []
    palavra.lower()
    for x in list(palavra):
        if x in 'aeiouáéíóúâêîôûàãõ':
            lista.append(x + 'p' + x)
        else:
            lista.append(x)
    return ''.join(lista)