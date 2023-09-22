def conta_frases(texto):
    """funcao que conta a quantidade de frases, sendo cada frase sendo finalizada por um tipo de caractere"""
    return texto.count('.')+\
           texto.count('...')+\
           texto.count('!')+\
           texto.count('?')