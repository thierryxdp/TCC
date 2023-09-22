def inverte(frase):
    'função que dada uma frase a retorna com as palavras na ordem inversa'
    import string
    frase = frase.translate(str.maketrans('', '', string.punctuation))
    frase = frase.lower()
    separar = str.split(frase)
    lista = separar[::-1]
    frase_final = str.join(' ', lista)
    return frase_final