def retira_pontuacao(x):
    '''Retorna uma frase sem caracteres de pontuação.
    str -> str'''
    a=str.find(x,'-')
    b=str.find(x,',')
    c=str.find(x,':')
    d=str.find(x,'.')
    e=str.find(x,',')
    x=x-x(a)-x(b)-x(c)-x(d)-x(e)
    return x