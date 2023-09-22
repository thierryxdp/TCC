def retira_pontuacao(x):
    ''' função que dada uma frase retorna-a sem os caracteres de pontuação'''
    '''str->str'''
    x=str.replace(x,'-',' ')
    x=str.replace(x,',',' ')
    x=str.replace(x,';',' ')
    x=str.replace(x,':',' ')
    x=str.replace(x,'.',' ')
    x=str.replace(x,'!',' ')
    x=str.replace(x,'?',' ')
    return x