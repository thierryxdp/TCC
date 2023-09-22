def retira_pontuacao(frase):
    """retorna a frase onde todos os caracteres de pontuação tenham sido substituidos por espaços; str -> str"""
    x=str.replace(frase,'-',' ')
    y=str.replace(x,',',' ')
    z=str.replace(y,':',' ')
    w=str.replace(z,';',' ')
    a=str.replace(w,'.',' ')
    b=str.replace(a,'!',' ')
    c=str.replace(b,'?',' ')
    d=str.replace(c,'...',' ')
    return d