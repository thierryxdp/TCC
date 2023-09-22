def retira_pontuacao(frase):
    """ Substitui as pontuações de uma frase por espaços.
assinatura: str
"""
    t = (str.replace(frase,"-"," "))
    v = (str.replace(t,","," "))
    d = (str.replace(v,":"," "))
    p = (str.replace(d,";"," "))
    f = (str.replace(p,"..."," "))
    e = (str.replace(f,"!"," "))
    i = (str.replace(e,"?"," "))
    r = (str.replace(i,"."," "))
    return r