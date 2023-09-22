def lingua_p(palavra):
    """Função que converter uma palavra para lingua do P."""
    """String -> String"""
    palavrap = ''
    for letra in palavra:
        if letra in "AÁÀÃÂaãâáàEÉÈeéèIÍÌiíìOÓÒoóòUÚÙuúù":
            palavrap += letra + "p" + letra
        else:
            palavrap += letra
    return palavrap