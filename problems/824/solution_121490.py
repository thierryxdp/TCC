def uppCons(frase):
    """Determinar uma string com todas consoantes maiúsculas;
    string -> string"""
    frase_nova = ""
    for letra in frase:
        if letra.lower() in "bcçdfghjklmnpqrstvwxyz":
            frase_nova += letra.upper()
        else:
            frase_nova += letra
    return frase_nova