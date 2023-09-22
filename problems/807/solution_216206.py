def conta_frases(frase):
    '''Função que recebe um texto armazenado em uma string(frase);
    e retorna seu número de frases considerando sua pontuação.
    str-> int'''
    frase = frase.replace('...', '.')
    frase = frase.replace('!', '.')
    frase = frase.replace('?', '.')
    frase = frase.split('.')
    return len(frase)-1