def conta_frases(texto):
    """ dado o texto, retornar a quantidade de frases contidas nele"""
    return str.count(texto,".")+ str.count(texto,"!")+str.count(texto,"?")+str.count(texto,"...")