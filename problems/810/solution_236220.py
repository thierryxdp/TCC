def inverte(frase):
    """inverte a frase de entrada"""
    frase=frase.replace(";","#")
    frase=frase.replace("!","#")
    frase=frase.replace("?","#")
    frase=frase.replace(".","#")
    frase=frase.replace(":","#")
    frase=frase.replace(",","#")
    frase=frase.replace("-","#")
    str.lower(frase)
    s=str.replace(frase,"#"," ")
    str.split(s)
    return s[-1::-1]