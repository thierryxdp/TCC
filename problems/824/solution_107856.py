def uppCons(frase):
    """Função que recebe como entrada uma frase e retorne ela com todas as suas consoantes em maiusculas e os demais da maneira como estavam antes
       str -> str"""
    s = " "
    for caractere in frase:
        if caractere in "bcdfghjklmnpqrstvwxyz":
            s += caractere.upper()
        else:
            s += caractere
    return s