def conta_frases(y):
    '''Informando um texto, tal funcao conta quantas frases estao presentes nesses
           str->int'''
    return str.count(y,'.')+str.count(y,'!')+  str.count(y,'?')- + str.count(y,'...')*2