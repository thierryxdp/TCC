def conta_frase(x):
    """
Função que dado uma strng conta as frases a partir dos pontos '.', '!', '?', '...'
"""
    r = int()
    if "." in str(x):
        r = r + len(str.split(x,"."))
    if "?" in str(x):
        r = r + len(str.split(x,"?"))
    if "..." in str(x):
        r = r + len(str.split(x,"..."))
    if "!" in str(x):
        r = r + len(str.split(x,"!"))
    return r