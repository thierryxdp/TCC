def inverte (frase):
    """ """
    frase=str.lower(frase)
    a=frase.replace("!","").replace(".","").replace("...","").replace(";", "").replace (":", "").replace(",","").replace("?","").replace("-","") 
    a=str.split(frase)
    a=a[::-1]
    str.join(a)
    return a