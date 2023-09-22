def conta_frases(s):
    '''Função que retorna o número de frases na string de entrada'''
    return str.count(s,',')+str.count(s,'.')+str.count(s,'...')+str.count(s,'!')+str.count(s,'?')