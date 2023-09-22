def retira_pontuacao(texto):
    '''função que dada uma string retira a sua pontuação
    valor de entrada: str
    valor de saída: str'''
    
    textomudado1=texto.replace('-',' ')
    textomudado2=textomudado1.replace(',',' ')
    textomudado3=textomudado2.replace('!',' ')
    textomudado4=textomudado3.replace('?',' ')
    textomudado5=textomudado4.replace(';',' ')
    textomudado6=textomudado5.replace('.',' ')
    textomudado7=textomudado6.replace(':',' ')
    
    return textomudado7


def inverte(texto):
    '''asdasds
    valor de entrada:
    valor de saída:'''
    fraseminuscula=str.lower(retira_pontuacao(texto))
    frasecorrigida=str.split(fraseminuscula)[::-1]
    frasefinal= str.join(' ',frasecorrigida)