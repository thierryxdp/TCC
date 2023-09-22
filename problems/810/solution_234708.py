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

def inverte(frase):
    """ função que dada uma frase retorne outra frase com as mesmas palavras só que na ordem inversa e sem a pontuação"""
x= str.lower(retira_pontuacao(frase))
y= str.split(x," ")
z= str.join(y," ")
return z