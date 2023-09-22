def uppCons(frase):
    """	Recebe uma frase como entrada e retorna todas suas consoantes
    em letras maiúsculas.
    asssinatura: str --> str"""
    num = 0
    while num < len (frase):
        if frase [num] in "bcdfghjklmnpqrstvwxyz":
            str.upper (frase [num])
        num += +1
        return frase