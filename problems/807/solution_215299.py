def conta_frases(texto):
    """função que conta o número de frases que aparece em um texto
 str--->int"""
    s = str.replace(str.replace(str.replace(texto,"...","@"),"!","@"),"?","@")
    s_ = str.replace(s,".","@")
    frases = str.count(s_,"@",0)
    return frases