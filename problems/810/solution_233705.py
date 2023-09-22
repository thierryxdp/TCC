def inverte(frase):
    """dada uma frase retorna outra frase que conenha as mesmas palavras na ordem inversa se letras maiusculas e sem pontuação; string-> string"""
    lista = str.split(frase)
    invert = lista[::-1]
    sep = str.join(' ', invert)
    return sep