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

def inverte(frase):
    '''função que dada uma frase retorna a sua versão invertida'''
    '''str->str'''
    frase=str.lower(frase)
    frase=retira_pontuacao(frase)
    frase=str.split(frase,' ')
    list.reverse(frase)
    frase=str.join(frase)
    return frase