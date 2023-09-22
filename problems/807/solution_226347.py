def conta_frases(texto):
    """ dado o texto, retornar a quantidade de frases contidas nele"""
    if '...' in texto:
        return str.count(texto,".")+ str.count(texto,"!")+str.count(texto,"?")+str.count(texto,'...')-3
    else:
        return str.count(texto,".")+ str.count(texto,"!")+str.count(texto,"?")+str.count(texto,'...')