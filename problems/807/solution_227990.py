def conta_frase(frase):
    '''Esta funçao conta o numero de frases em umm texto
    string===>int'''
    frase = frase.replace('...' , '$')
    frase = frase.replace('.' , '$')
    frase = frase.replace('!' , '$')
    frase = frase.replace('?' , '$')
    
    return (frase.count('$') - 1)