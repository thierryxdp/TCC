def conta_frases(texto):
    """ dado o texto, retornar a quantidade de frases contidas nele"""
    a="."
    return str.count(texto,a)+ str.count(texto,"!")+str.count(texto,"?")+str.count(texto,"...")