def inverte(frase):
    """ Substitui as pontuações de uma frase por espaços.
assinatura: str
"""
    h = (str.lower(retira_pontuacao(frase)))
    t = (str.split(h))
    list.reverse(t)
    t = str.join(" ",t)
    return t

def retira_pontuacao(frase):
    t = (str.replace(frase,"-"," "))
    v = (str.replace(t,","," "))
    d = (str.replace(v,":"," "))
    p = (str.replace(d,";"," "))
    f = (str.replace(p,"..."," "))
    e = (str.replace(f,"!"," "))
    i = (str.replace(e,"?"," "))
    r = (str.replace(i,"."," "))
    return r