def inverte(frase):
    """Essa função recebe uma frase, remove sua pontação e a inverte
    str -> str"""
    frase = remove_pontuacao(frase)
    frase = frase.lower()
    frase = frase.split()
    frase.reverse()
    frase = " ".join(frase)
    return(frase)