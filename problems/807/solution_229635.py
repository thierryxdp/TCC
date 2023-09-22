def conta_frases(texto):
    frase1 = texto.split('.')
    frase2 = texto.split('!')
    frase3 = texto.split('?')
    frase4 = texto.count('...')
    
    return (len(frase1) - 2 * frase4) + len(frase2) + len(frase3) - 3