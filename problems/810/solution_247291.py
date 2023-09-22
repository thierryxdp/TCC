def inverte(frase):
    """
    Código que inverte a ordem de palavras da entrada frase
    sem letras maiúsculas e sem pontuação.
    :Frase --> String:
    :Return--> String:
    """
    frase_v1 = frase.lower()
    frase_v2 = frase_v1.split()[::-1]
    frase_v3 = '.'.join(frase_v2)
    return frase_v3