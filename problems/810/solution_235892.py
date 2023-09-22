def inverte (frase):
    """ """
    frase=str.lower(frase) 
    a=str.split(frase)
    frase=frase.replace("!","").replace(".","").replace("...","").replace(";", "").replace(":","").replace(",","").replace("?","").replace("-","") 
    a=a[::-1]
    str.join(a, frase)
    return a