def retira_pontuacao(n):
    n = n.replace('...',' ')
    n = n.replace('!',' ')
    n = n.replace('?',' ')
    n = n.replace('.',' ')
    n = n.replace('-',' ')
    n = n.replace(',',' ')
    n = n.replace(':',' ')
    n = n.replace(';',' ')
    return n