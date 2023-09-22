def conta_frases(frase):
    '''
       Funcao que retorna o numero de frases que aparecem no texto
       str -> int
    '''
    frase1 = frase.split('.')
    frase2 = frase.split('!')
    frase3 = frase.split('?')
    frase4 = frase.count('...')

    return (len(frase1) - 2*frase4) + len(frase2) + len(frase3) - 3