def conta_frases(texto):
    """ dado o texto, retornar a quantidade de frases contidas nele"""
    if "..." in texto:
        texto= str.replace(texto,"...","@")
        a=str.count(texto,"@")
        return a+str.count(texto,".")+ str.count(texto,"!")+str.count(texto,"?")