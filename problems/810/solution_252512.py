def inverte(Frase):
    """Retorna a frase de entrada(Frase) invertida, em letras minúsculas e sem pontuação.
    str -> str"""
    Frase1 = Frase.rstrip(".!?").split(",")
    Frase1 = ''.join(Frase1).split("-")
    Frase1 = ' '.join(Frase1)
    Frase1 = Frase1.lower().split()[::-1]
    return ' '.join(Frase1)