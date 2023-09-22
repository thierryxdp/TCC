def retira_pontuacao(frase):
    """função que dada uma frase, retorne a frase onde todos os caracteres de pontuação
    tenham sido substituidos por espaço"""
    a= str.replace(frase("-"," "))
    b=str.replace(a,(","," "))
    c=str.replace(b,(":"," "))
    d=str.replace(c,(";"," "))
    e=str.replace(d,("."," "))
    f=str.replace(e,("?"," "))
    g=str.replace(f,("!"," "))
    return g