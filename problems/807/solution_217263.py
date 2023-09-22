def conta_frases(frase):
    """função que recebe uma string com uma frase e a função
    retorna a quantidade de frases.
    str -> <quant_frase>>"""
    frase = frase.replace('!','.')
    frase = frase.replace('...','.')
    frase = frase.replace('?','.')
    frase = frase.split('.')
    quant_frase = len(frase) - 1

    return quant_frase