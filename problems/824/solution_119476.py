def uppCons(x):
    """A função pega a string "X" e a modifica para que as suas consoantes fiquem maiúsculas
    str --> str"""
    r = ""
    for frase in x:
        if frase in "bcdfghjklmnqstvwxyz":
            r = r + str.upper(frase)
        else:
            r = r + frase
       
     
    return r