def uppCons(frase):
    """Dada  uma frase transforma as
    suas consoantes em maiúsculas
    str -> str"""
    newfrase = ''
    i=0
    while i<len(frase):
        c=frase[i]
        if c in 'bcdfghjklmnpqrstwxyzç:
            c = str.upper(c)
        newfrase = newfrase + c
        i=i+1
    return frase_tratada