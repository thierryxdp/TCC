def inverte(frase):
    """ """
    contador=frase.replace("-"," ").replace(","," ").replace(":"," ").replace(";"," ").replace("!"," ").replace("."," ").replace("?"," ")
    contador2= contador.split("/")
    contador3= contador2.join("/",contador2)
    return contador3