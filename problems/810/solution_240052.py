def inverte (frase):
    """retorne a frase de entrada transcrita contendo as mesmas palavras da frase de entrada na ordem inversa"""
    palavras = frase.split()
    palavras.reverse()
    return ' '.join(palavras)