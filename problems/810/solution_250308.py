def retira_pontuacao(x):
    """A função tira os caracteres de pontuação da string como retorno e
sua entrada deve ser uma string.string-->string"""
    a=str.replace(x,"..."," ")
    z=str.replace(a,"."," ")
    b=str.replace(z,","," ")
    c=str.replace(b,":"," ")
    d=str.replace(c,";"," ")
    e=str.replace(d,"-"," ")
    f=str.replace(e,"?"," ")
    g=str.replace(f,"!"," ")
    return g

def inverte(x):
    """ A função inverte a ordem das palavras da string de entrada. string-->string""" 
    g = retira_pontuacao(x)
    h=str.split(g)
    i=h[::-1]
    return str.lower(str.join(" ",i))