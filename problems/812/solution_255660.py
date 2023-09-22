def retira_pontuacao(frase):
    """função que, dada uma frase, retorne a frase onde todos os caracteres
    de pontuação, incluidno travessão,virgula,dois pontos,ponto e virgula,
    alem da pontuação de final de frase, tenham sido substituidos por
    espaço.
    str -> str
    """

    a = str.replace(frase,'...',' ')
    b = str.replace(a,',',' ')
    c = str.replace(b,'-',' ')
    d = str.replace(c,':',' ')
    e = str.replace(d,'?',' ')
    f = str.replace(e,'!',' ')
    g = str.replace(f,'.',' ')
    h = str.replace(g,';',' ')
    return h