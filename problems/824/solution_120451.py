def uppCons(frase):
    """retorna uma frase com todas suas consoantes em maiusculas e os demais caracteres
    como estavam na frase original;
    str -> str"""
    i = 0
    texto = " "
    while i < len(frase):
        if frase[i] in "bcçdfghjklmnpqrstvwxyz":
            texto = texto+str.upper(frase[i])
        else:
            texto = texto+frase[i]
        i = i+1
    return texto