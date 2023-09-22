def inverte(frase):
    """ """
    contador=frase.replace("-"," ").replace(","," ").replace(":"," ").replace(";"," ").replace("."," ").replace("?"," ").replace("!"," ")
    contador2=str.lower(contador)
    contador3=str.split(contador2)
    contador4=str.join[contador3]
    return str.join(" ",contador4)