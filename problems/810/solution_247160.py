def inverte(texto):
    '''Função que retorna uma frase de maneira invertida sem letras maiusculas e sem pontuação'''
    'str --> str'
    texto=list(texto)
    texto1 = str.replace(texto,'...','.')
    texto2 = str.replace(texto1,'!','.')
    texto3 = str.replace(texto2,'?','.')
    T=list(texto3)
    return list.reverse(T)