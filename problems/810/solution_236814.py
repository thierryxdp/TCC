def inverte(frase):
    """ """
    contador=frase.replace("-"," ").replace(","," ").replace(":"," ").replace(";"," ").replace("!"," ").replace("?"," ").replace("."," ")
    contador2=str.lower(contador)
    contador3=frase[::-1]
    return contador3