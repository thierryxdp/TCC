def inverte (frase):
    """ """
    frase=str.lower(frase) 
    frase=frase.replace("!","").replace(".","").replace("...","").replace(";", "").replace(":","").replace(",","").replace("?","").replace("-","") 
    a=str.split(frase)
    a=a[::-1]
    a=" ".join(a)
    return a