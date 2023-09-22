def conta_frases(text):
    """ Conta o número de frases existentes na função
         str->int"""
    v1 = str.replace(text, '...', '.')
    pontoF = len(str.split(v1,'.'))-1
    pontoE = len(str.split(text,'!'))-1
    pontoI = len(str.split(text,'?'))-1
    soma = ponto F + pontoE + pontoI
    return soma