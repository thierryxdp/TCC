def retira_pontuacao(x):
    '''retira a pontuação dada na frase e retorna espaço'''
    a = str.replace(x, '.',' ')
    b = str.replace(a, ',',' ')
    c = str.replace(b, '!',' ')
    d = str.replace(c, ':',' ')
    e = str.replace(d, ';',' ')
    f = str.replace(e, '?',' ')
    g = str.replace(f, '-',' ')
    
    return g