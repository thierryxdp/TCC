def inverte(frase):
    """inverte a frase de entrada"""
    str.lower(frase)
    frase=frase.replace(";","#")
    frase=frase.replace("!","#")
    frase=frase.replace("?","#")
    frase=frase.replace(".","#")
    frase=frase.replace(":","#")
    frase=frase.replace(",","#")
    frase=frase.replace("-","#")
    frase=str.replace(frase,"#"," ")
    frase.split(" ")
    frase.pop()
    frase.split(" ")[::-1]
    frase=str.lower(frase)
    return " ".join(frase.split(" ")[::-1])