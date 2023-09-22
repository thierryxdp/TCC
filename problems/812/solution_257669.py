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