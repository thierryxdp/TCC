def inverte(frase):
    """Essa função recebe uma frase, remove sua pontuação e a inverte
    str -> str"""
    frase = remove_pontuaação(frase)
    frase = frase.lower()
    frase = frase.split()
    frase.reverse()
    frase = " ".join(frase)
    return(frase)