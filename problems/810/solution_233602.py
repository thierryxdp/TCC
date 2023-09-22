def inverte(frase):
    '''dada uma frase, retorna outra com as palavras na ordem inversa
    str -> str'''
    separada = str.split(frase, ' ')
    return str.join (' ',separada)