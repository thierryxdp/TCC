def retira_pontuacao(txt):
    x = txt.replace('-',' ')
    x = x.replace(',',' ')
    x = x.replace(':',' ')
    x = x.replace(';',' ')
    x = x.replace('.',' ')
    return x