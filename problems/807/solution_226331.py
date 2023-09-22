def conta_frases(texto):
    """ dado o texto, retornar a quantidade de frases contidas nele"""
    if "." in texto:
        a= str.count(texto,".")
    if "!" in texto:
        b= str.count(texto,"!")
    if "?" in texto:
        c= str.count(texto,"?")
    if "..." in texto:
        d= str.count(texto,"...")
    return a+b+c+d