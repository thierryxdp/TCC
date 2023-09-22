def conta_frases(frase):
    x = frase.split('?')
    z = frase.split('!')
    y = frase.split('.')
    
    if '?' in frase and  '.' in frase:
        return len( frase)