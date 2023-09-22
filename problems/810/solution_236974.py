def inverte(frase):
    """ """
    contador=frase.replace("-"," ").replace(","," ").replace(":"," ").replace(";"," ").replace("."," ").replace("?"," ").replace("!"," ")
    contador2=str.lower(contador)
    contador3=str.split(contador2)
    contador4=contador3[::-1]
    return str.join(" ",contador4)