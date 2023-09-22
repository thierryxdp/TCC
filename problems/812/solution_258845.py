def retira_pontuacao(frase):
    """Dada uma frase, retorna a frase onde todos os caracteres de
    pontuação sejam substituídos por espaço;
    string->string"""
    a=str.find(frase,'-')
    b=str.find(frase,',')
    c=str.find(frase,':')
    d=str.find(frase,';')
    e=str.find(frase,'.')
    f=str.find(frase,'!')
    g=str.find(frase,'?')
    x=[a,b,c,d,e,f,g]
    y=str.replace(frase,x,' ')
    return y