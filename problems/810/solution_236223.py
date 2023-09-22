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
    str.join(" ",s)
    return s[-1::-1]