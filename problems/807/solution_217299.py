def conta_fases(frase):
    """Dado um texto conta o número de frases;
    int->float"""
    return str.count(frase,"...")+(str.count(frase,".")-w*3)+str.count(frase,"!")+str.count(frase,"?")