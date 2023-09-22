def uppCons(frase):
    """Função que recebe como entrada uma frase e retorna ela com todas as suas consoantes em maiuscula e os demais caracteres exatamente como estavam na frase original
       str -> str"""
    uppCons.upper()
    return " ".join(uppCons.upper() if caractere in "bcdfghjklmnpqrstvwxyz" else caractere for caractere in frase)