def conta_frases(texto):
    frase1 = texto.count('.')
    frase2 = texto.count('!')
    frase3 = texto.count('?')
    frase4 = texto.count('...')
    
    return frase1+frase2+frase3+frase4