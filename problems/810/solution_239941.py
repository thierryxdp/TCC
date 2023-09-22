def inverte(frase):
    """ """
    lista = (str.split(str.replace(str.replace(str.replace(str.replace(str.replace(frase,'.',' '),'!',' '),'?',' '),',',' '),'-',' ')))
    return  str.lower(str.join(" ",(lista[::-1])))