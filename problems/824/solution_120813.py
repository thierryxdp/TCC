def uppCons(frase):
    """Retorna uma string com todas consoantes maiúsculas;
    string -> string"""
    frase_nova = ""
    for letra in frase:
        if letra.lower() in "bcdfghjklmnpqrstvwxyz":
            frase_nova += letra.upper()
        else:
            frase_nova += letra
    return frase_nova