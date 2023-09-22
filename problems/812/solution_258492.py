def retira_pontuacao(f):
    r = '...'
    if r in f:
        r = '.'
    f1 = f.replace('.',' ')
    f1 = f.replace('!',' ')
    f1 = f.replace('?',' ')
    f1 = f.replace('-',' ')
    f1 = f.replace(',',' ')
    f1 = f.replace(':',' ')
    f1 = f.replace(';',' ')
    return f1