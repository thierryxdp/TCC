def conta_frases (texto):
    '''Função que, dado um texto, calcula e retorna
    a quantidade frases de presentes, cada frase é 
    separada por uma certa pontuação('.' ; '!' ; '?' ; '...'), 
    e retorna o número
    de frases presente
    str --> int'''
    return texto.count('!') + texto.count('.') + texto.count('?') - 2*texto.count('...')