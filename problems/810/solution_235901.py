def inverte (frase):
    """ """
    frase=str.lower(frase) 
    frase=frase.replace("!","").replace(".","").replace("...","").replace(";", "").replace(":","").replace(",","").replace("?","").replace("-","") 
    a+b=str.split(frase)
    a+b=a+b[::-1]
    a=str.join(a+b)
    return a