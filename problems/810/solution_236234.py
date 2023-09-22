def inverte(frase):
    """inverte a frase de entrada"""
    str.lower(frase)
    frase=frase.replace("!","#")
    frase=frase.replace("?","#")
    frase=frase.replace(".","#")
    frase=frase.replace(",","#")
    frase=frase.replace("-","#")
    frase=str.replace(frase,"#"," ")
    frase.split(" ")
    frase.split(" ")[::-1]
    frase=str.lower(frase)
    frase=" ".join(frase.split(" ")[::-1])
    return frase[1:]