def quant_palavras(frase):
    """Função que retorna o número de palavras em uma frase
         str=> int"""
    x = frase.split()
    numero = len(x)
    return numero
    
    ''' frase.split() transforma a string em uma lista em que cada palavra
    é um elemento, e len(x) conta o número de elementos na string. '''