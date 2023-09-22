def uppCons(frase):
    """	Recebe uma frase como entrada e retorna todas suas consoantes
    em letras maiúsculas.
    asssinatura: str --> str"""
    final = ''
    num = 0
    while num < len (frase):
        if frase [num] in "bcdfghjklmnpqrstvwxyz":
            final += str.upper (frase [num])
        else:
            final += frase [num]
        num += 1
        return final