def inverte (frase):
    """retorne a frase de entrada transcrita contendo as mesmas palavras da frase de entrada na ordem inversa"""
    frase= frase.split()
    frase= frase.replace('!','  ')
    frase.reverse()
    return ' '.join(frase)