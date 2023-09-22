def conta_frases(frase):
    """Dado um texto conta o número de frases;
    int->float"""
    w=str.count(frase,"...")
    x=(str.count(frase,".")-w*3)
    y=str.count(frase,"!")
    z=str.count(frase,"?")
    return w+x+y+z