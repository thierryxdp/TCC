def conta_frases(frase):
    '''
       Funcao que retorna o numero de frases que aparecem no texto
       str -> int
    '''

    return (len(frase.split('.'))-2*frase.split('...'))+len(frase.split('!'))+len(frase.split('?'))-3