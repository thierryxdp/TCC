def retira_pontuacao(f):
        f=f.replace(',',' ')
        f=f.replace('.',' ')
        f=f.replace('-',' ')
        f=f.replace(':',' ')
        f=f.replace(';',' ')
        return f