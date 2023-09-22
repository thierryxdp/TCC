def inverte(frase):
    """
    Código que inverte a ordem de palavras da entrada frase
    sem letras maiúsculas e sem pontuação.
    :Frase --> String:
    :Return--> String:
    """
    if (str.lower in str(frase)):
        return str.upper