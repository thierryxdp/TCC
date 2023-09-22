def conta_frases(frase):
    """Para saber quantas frases o texto possui, digite;
    str-> int"""
    
    A=frase.replace("." , "#")
    B=frase.replace ("..." , "#")
    C=frase.replace ("!", "#")
    D=frase.replace("?", "#")
    
    return A.count(frase,"#")+B.count(frase,"#")+C.count(frase,"#")+D.count(frase,"#")