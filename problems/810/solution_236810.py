def inverte(frase):
    """ """
    contador=frase.replace("-"," ").replace(","," ").replace(":"," ").replace(";"," ").replace("!"," ").replace("?"," ")
    contador2=str.lower(contador)
    return contador2