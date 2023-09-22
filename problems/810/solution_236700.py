def inverte(frase):
    """ """
    contador=frase.replace("-"," ").replace(","," ").replace(":"," ").replace(";"," ").replace("!"," ").replace("."," ").replace("?"," ")
    contador2= contador.split("/")
    contador3= str.lower(contador2)
    return contador3