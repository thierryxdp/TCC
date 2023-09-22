def retira_pontuacao(frase):
    x=str.replace(frase,'.',' ') and
    x=str.replace(frase,',',' ')
    z=str.replace(frase,':',' ')
    w=str.replace(frase,';',' ')
    t=str.replace(frase,'!',' ')
    u=str.replace(frase,'?',' ')
    v=str.replace(frase,'-',' ')
    return x