def conta_frases(frase):
    """Para saber quantas frases o texto possui, digite;
    str-> int"""

    X=frase.replace("..." , "#"), frase.replace ("." , "#")
    Y=frase.replace ("!", "#"),frase.replace("?", "#")
    return ((X.count(frase,"#")+Y.count(frase,"#"))