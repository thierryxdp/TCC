def conta_frases(frase):
    numFrases=0
    frase=frase.replace('...','.')
    numFrases+=frase.count('.')
    numFrases+=frase.count('!')
    numFrases+=frase.count('?')
    numFrases+=frase.count(',')
    numFrases+=frase.count('.')
    return numFrases