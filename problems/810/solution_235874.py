def inverte (frase):
    """ """
    frase=str.lower(frase)
    a=str.split(frase)
    a=a[::-1]
    a=a.replace("!","").replace(".","").replace("...","").replace(";", "").replace (":", "").replace(",","").replace("?","").replace("-","") 
    str.join(a)
    return a