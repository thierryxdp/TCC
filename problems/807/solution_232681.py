def conta_frases(frase):
    """funçao que calcula o numero de frases que aparecem
    em determinado texto"""
    frase=str.replace(frase,'!','/')
    frase=str.replace(frase,'...','/')
    frase=str.replace(frase,'.','/')
    frase=str.replace(frase,'?','/')
    texto=str.split(frase,'/')
    numero=len(texto)-1
    return numero