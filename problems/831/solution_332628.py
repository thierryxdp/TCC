def lingua_p(palavra):
    '''Recebe uma <palavra> (em portugues) e 
    retorna a mesma palavra na lingua do P, 
    isto é, após cada vogal da palavra original
    é inserida a sequencia de letras 'p' mais a
    vogal original
    
    str -> str
    '''
    traduzido_p = []
    contador = 0 
    
    for letra in list(palavra):
        if letra in 'aeiouáéíóú':
            traduzido_p.append(letra + 'p' +letra)
        else:
            traduzido_p.append(letra)
    return ''.join(traduzido_p)