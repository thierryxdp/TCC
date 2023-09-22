def retira_pontuacao(text):
    ''' Função que retira a pontuação(travessão,vírgla,dois ponto,ponto e vírgula ect.)
    de um texto, text. str->str'''
    a=str.replace(text,':',' ')
    b=str.replace(a,'-',' ')
    c=str.replace(b,',',' ')
    d=str.replace(c,';',' ')
    e=str.replace(d,'?',' ')
    f=str.replace(e,'!',' ')
    g=str.replace(f,'.',' ')
    h=str.replace(g,'...',' ')
    return h

def inverte(fr):
    ''' Função que inverte uma frase, fr, e retira sua pontuação'''
    limpo=retira_pontuacao(fr)
    corte=str.split(limpo)
    return str.join(' ',reversed(corte))