def inverte(frase):
    """inverte a frase de entrada"""
    frase=frase.replace(";","#")
    frase=frase.replace("!","#")
    frase=frase.replace("?","#")
    frase=frase.replace(".","#")
    frase=frase.replace(":","#")
    frase=frase.replace(",","#")
    frase=frase.replace("-","#")
    s=str.replace(frase,"#"," ")
    str.split(s)
    t=s[:0:-1]
    return t[::-1]