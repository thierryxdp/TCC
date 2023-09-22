def conta_frases(txt):
    ''' Retorna a quantidade de frases de um texto
    str -> int '''
    return (txt.count('.') - (txt.count('...') * 2)) +  txt.count('!') + txt.count('?')