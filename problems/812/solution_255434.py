def retira_pontuacao(frase):
    """dada uma frase, retorna a frase com a pontuação subistituida por espaço
    str->str"""
    a=str.replace(frase,'...',' ')
    b=str.replace(a,'?',' ')
    c=str.replace(b,'.',' ')
    d=str.replace(c,'!',' ')
    e=str.replace(d,',',' ')
    f=str.replace(e,'-',' ')
    g=str.replace(f,';',' ')
    h=str.replace(g,':',' ')
    return h