def conta_frases(texto):
    '''função que dado um texto, retorna a quantidade de frases contida nele;
    str -> int'''
    separa1 = len(texto.split('...'))
    separa2 = len(texto.split('!'))
    separa3 = len(texto.split('?'))
    separa4 = len(texto.split(';'))
    separa5 = len(texto.split('...'))
    frases = separa1 + separa2 + separa3 + separa4 - separa5
    return frases