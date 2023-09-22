def uppCons(frase):
    """Retorna a frase dada na entrada com todas as suas consoantes em maiúsculo.
    str->str"""
    c=0
    f=""
    while c<len(frase):
        if frase[c]in "bcdfghjklmnpqrstvwxzç":
            f+=str.upper(frase[c])
        else:
            f+=frase[c]
        c=c+1
    return f