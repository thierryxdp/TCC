def inverte(frase):
    """Função, que dada uma frase, retorna outra que contenha as mesmas palavras na ordem inversa, sem letras maiusculas e pontuação."""
    """str->str"""
    for x in ".!?,;:-":
        frase = frase.replace(x, "")
    frase_nova = str.lower(frase)
    return frase_nova[::-1]