def retira_pontuacao(f):
    r = '...'
    if r in f:
        r = '.'
    f1 = f.replace('.',' ')
    f2 = f1.replace('!',' ')
    f3 = f2.replace('?',' ')
    f4 = f3.replace('-',' ')
    f5 = f4.replace(',',' ')
    f6 = f5.replace(':',' ')
    f7 = f6.replace(';',' ')
    return f7