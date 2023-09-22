def retira_pontuacao(x):
    '''função que dada uma frase retorna uma frase em que os caracteres de
    pontuação são substituidos por espaço'''
    a=str.replace(x,'.',' ')
    b=str.replace(a,':',' ')
    c=str.replace(b,';',' ')
    d=str.replace(c,',',' ')
    e=str.replace(d,'-',' ')
    return e