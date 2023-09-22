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

def inverte(frase):
    '''inverte a ordem da frase chamada, sem pontuacao e sem letras maiusculas;
    str->str'''
    a=retira_pontuacao(frase)
    b=str.lower(a)
    c=str.split(b)
    return str.join(' ',(c[::-1]))