def conta_frases(texto):
    '''conta o número de frases em um texto'''
    frases1=list(texto.split('.'))
    frases2=list(texto.split('!'))
    frases3=list(texto.split('?'))
    frases=frases1+frases2+frases3
    return len(frases)