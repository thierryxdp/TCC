def retira_pontuacao(frase):
    '''função que dado uma frase como entrada, retorne a frase onde os
    caracteres de pontuação tenham sido substituidos por espaço'''
    s=frase
    a=str.replace(s,'.',' ')
    b=str.replace(a,',',' ')
    c=str.replace(b,':',' ')
    d=str.replace(c,'-',' ')
    e=str.replace(d,';',' ')
    f=str.replace(e,'...',' ')
    g=str.replace(f,'!',' ')
    h=str.replace(g,'?',' ')
    return h