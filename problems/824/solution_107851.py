def uppCons(frase):
    """Função que recebe como entrada uma frase e retorna ela com todas as suas consoantes em maiuscula e os demais caracteres exatamente como estavam na frase original
       str -> str"""
    s = " "
    for caractere in frase:
        if caractere in "bcdfghjklmnpqrstvwxyz":
            s += caractere.upper()
        else:
            s += caractere
        return s