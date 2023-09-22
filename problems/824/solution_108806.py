def uppCons(frase):
    """A função recebe como entrada uma frase e retorna a frase com todas
    as suas consoantes maiúsculas, mantendo os demais caracteres exatamente
    como estavam na frase original;
    str -> str"""
    frase_nova = ""
    i = 0
    while i<len(frase):
        if frase[i] in "AEIOUaeiou":
            frase_nova = frase_nova + frase[i]
        elif frase[i] not in "AEIOUaeiou":
            frase_nova = frase_nova + str.upper(frase[i])
        i = i + 1
    return frase_nova