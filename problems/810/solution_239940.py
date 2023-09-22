def inverte(frase):
    """ """
    lista = str.lower(str.split(str.replace(str.replace(str.replace(str.replace(str.replace(frase,'.',' '),'!',' '),'?',' '),',',' '),'-',' ')))
    return  str.join(" ",(lista[::-1]))