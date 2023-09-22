def uppCons(frase):
    """Função que recebe como entrada uma frase e retorne ela com todas as suas consoantes em maiusculas e os demais da maneira como estavam antes
       str -> str"""
    i = 0
    s =" "
    while i < len(frase):
        if str.lower(frase[i]) in "aeiouáéíóúàãõâêô":
            s += frase[i]
        else:
            s += str.upper(frase[i])
        i += 1
    return s