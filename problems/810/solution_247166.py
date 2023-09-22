def inverte(frases):
    '''Função que retorna uma frase de maneira invertida sem letras maiusculas e sem pontuação'''
    'str --> str'
    novafrase1 = str.replace(frases,'...','.')
    novafrase2 = str.replace(novafrase1,'!','.')
    novafrase3 = str.replace(novafrase2,'?','.')
    novafrase4 = str.replace(novafrase3,'.','')
    novafrase5 = str.replace(novafrase4,'-','')
    novafrase6 = str.split()
    novafrase7 = (novafrase6)
    return novafrase7