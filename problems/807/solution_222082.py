def conta_frases (texto):
    '''Função que recebe um texto (texto) e retorna o
    numero de frases que aparece no texto. uma frase é
    formada pelo uso de um desses pontos no final de uma
    palavra: '.', '...', '?' e '!';
    str -> int
    '''
    if '...' in texto:
        return texto.count('.')+texto.count('...')+texto.count('!')+texto.count('?')
    else:
        return texto.count('.')+texto.count('!')+texto.count('?')