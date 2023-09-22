def retira_pontuacao(x):
    """A função tira os caracteres de pontuação da string como retorno e
sua entrada deve ser uma string.string-->string"""
    a=str.replace(x,"."," ")
    b=str.replace(a,","," ")
    c=str.replace(b,":"," ")
    d=str.replace(c,";"," ")
    e=str.replace(d,"-"," ")
    f=str.replace(e,"?"," ")
    g=str.replace(f,"!"," ")
    return g