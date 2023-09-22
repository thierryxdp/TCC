def inverte (frase):
    """ """
    frase=frase.replace("!","").replace(".","").replace("...","").replace(";", "").replace(":","").replace(",","").replace("?","").replace("-","") 
    frase=str.lower(frase) 
    a=str.split(frase)
    a=a[::-1]
    str.join(a, frase)
    return a