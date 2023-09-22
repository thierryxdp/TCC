def retira_pontuacao(text):
    ''' Função que retira a pontuação(travessão,vírgla,dois ponto,ponto e vírgula ect.)
    de um texto, text. str->str'''
    a=str.replace(text,':',' ')
    b=str.replace(text,'-',' ')
    c=str.replace(text,',',' ')
    d=str.replace(text,';',' ')
    e=str.replace(text,'?',' ')
    f=str.replace(text,'!',' ')
    g=str.replace(text,'.',' ')
    h=str.replace(text,'...',' ')
    return h