def retira_pontuacao(f):
    '''Retira todos os caracteres de pontuação de uma frase f
    str -> str'''
    l='abcdefghijklmnopqrstuvwxyz'
    L=list.upper(l)
    'x' in f:
        ('x' not in l) and ('x' not in L):
            str.replace(f,'x','')
    return f