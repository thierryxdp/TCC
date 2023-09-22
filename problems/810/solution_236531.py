def inverte (a):
    '''Retorna a frase sem pontuação e com as palavras na ordem inversa.
    str -> str'''
    l = str.split (pontuacao(a))
    return str.lower(str.join(' ', l[::-1]))