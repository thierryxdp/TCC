def inverte (frase):
    """ """
    frase=frase.remove("!").remove(".").remove("...").remove(";").remove(":").remove(",").remove("?").remove("-") 
    frase=str.lower(frase) 
    a=str.split(frase)
    a=a[::-1]
    str.join(a, frase)
    return a