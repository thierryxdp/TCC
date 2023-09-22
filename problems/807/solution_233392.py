def conta_frases(frase): 
    """conta o numero de frases que aparece"""
    aux = frase.count('!')
    aux2 = frase.count('?')
    aux3 = frase.count('...')
    aux4 = frase.count ('.') - aux3*3
    return aux+aux2+aux3+aux4