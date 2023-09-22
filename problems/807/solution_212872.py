def conta_frases(x):
    '''funcao que conte o numero dev frases que aparecem no texto,dado um texto armazenado uma string'''
    x = str.replace(x,"...","!")
    return str.count(x,".")+str.count(x,"!")+str.count(x,"?")