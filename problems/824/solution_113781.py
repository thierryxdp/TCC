def uppCons (frase):
    """ transforma todas as consoantes da frase em maiúsuclas"""
    list(frase)
    consoantes = list.index ('b','c','d','f')
    consoantes += list.index ('g','h','j')
    str(consoantes)
    cons_up = str.upper (consoantes)
    str.replace (frase, consoantes, cons_up)
    return frase