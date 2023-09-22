def inverte(frase):
    '''dada uma frase, retorna outra com as palavras na ordem inversa
    str -> str'''
    frase = str.lower (frase)
    lista = str.split(frase)
    return lista[-1::-1]