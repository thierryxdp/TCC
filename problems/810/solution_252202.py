def inverte(f):
    """Retorna a frase de entrada invertida, em minúsculas e sem pontuação.
    str -> str"""
    f2 = f.rstrip(".!?").split(",")
    f2 = ''.join(f2).split("-")
    f2 = ' '.join(f2)
    f2 = f2.lower().split()[::-1]
    return ' '.join(f2)