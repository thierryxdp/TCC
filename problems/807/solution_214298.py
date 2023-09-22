def conta frases(frase):
    x = frase.split('.')
    z= frase.split('?')
    y = frase.split('!')
    
    if '.' in frase:
        return len(x)