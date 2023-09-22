import re
def conta_frases(texto):
    '''Função que retorna o número de frases em um texto, sejam eles 
    terminadas por ponto final, ponto de exclamação, inrerrogação, ou 
    reticências.     str => int'''
    x = re.split('.|?|!|...',texto)
    numero = len(x)
    return numero