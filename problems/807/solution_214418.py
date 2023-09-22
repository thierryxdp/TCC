def conta_frases(frase):
    """calcula o numero de frases que aparecem no texto"""
    return ((frase.replace("...","#")
            .replace("?","#").replace("!","#")
            .replace(".","#")(str.count(frase,"#"))