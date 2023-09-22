def conta_frases(frase):
    """Para saber quantas frases o texto possui, digite;
    str-> int"""
    x=frase.replace("...","#"),frase.replace("?","#"),frase.replace(",","#")
    return str.count(x,"#")