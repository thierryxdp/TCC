def retira_pontuacao(a):
    #utilizando replace nas pontuações por espaços
    a=a.replace('...',' ')
    a=a.raplace('.',' ')
    a=a.replace('?',' ')
    a=a.replace('!',' ')
    a=a.replace('-',' ')
    a=a.replace(',',' ')
    a=a.replace(':',' ')
    a=a.replace(';',' ')
    return a