def retira_pontuacao(f):
        f.replace(',',' ')
        f.replace('.',' ')
        f.replace('-',' ')
        f.replace(':',' ')
        f.replace(';',' ')
    return f