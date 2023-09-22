def retira_pontuacao(frase):
    '''retira qualquer pontuacao das frases e substitui por espaços;
    str->str'''
    a=str.replace(frase,'-',' ')
    b=str.replace(a,',',' ')
    c=str.replace(b,':',' ')
    d=str.replace(c,';',' ')
    e=str.replace(d,'.',' ')
    f=str.replace(e,'!',' ')
    g=str.replace(f,'?',' ')
    h=str.replace(g,'...',' ')
    return h