def inverte (frase):
    """ """
    frase=str.lower(frase) 
    a=str.split(frase)
    a=frase.remove("!").remove(".").remove("...").remove(";").remove(":").remove(",").remove("?").remove("-") 
    a=a[::-1]
    str.join(a, frase)
    return a