def conta_frases(texto):
    """ dado o texto, retornar a quantidade de frases contidas nele"""
    if "." in texto:
        a= str.count(texto,".")
  
    elif "?" in texto:
        c= str.count(texto,"?")
    elif "..." in texto:
        d= str.count(texto,"...")
    return a+b+c+d