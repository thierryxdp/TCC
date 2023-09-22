def inverte(frase):
    """funçao que retorna outra frase com as mesmas palavras
    em ordem inversa
    str->"""
    frase = retira.pontuacao(frase)
    frase = frase.lower()
    frase = frase.split()
    frase.reverse()
    frase = " ".join(frase)
    return (frase)