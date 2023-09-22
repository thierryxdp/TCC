def retira_pontuacao(frase):
    """ função que, dada uma frase, retira toda a pontuação dela, substituindo por espaço"""
    x= str.replace(frase,("-"), " ")
    y=str.replace(x,(","), " ")
    z=str.replace(y,(":"), " ")
    w=str.replace(z,(";"), " ")
    r=str.replace(w,("."), " ")
    s=str.replace(r,("!"), " ")
    a=str.replace(s,("?"), " ")
    return a