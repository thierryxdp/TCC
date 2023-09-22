def uppCons(frase):
    """retorna a frase com todas as suas consoantes em maiúsculas; str -> str"""
    a='bcdfghjklmnpqrstvwxyz'
    b=0
    while b<len(frase):
        c=a[b]
        x=str.upper(c)
        str.replace(frase,c,x)
        b=b+1
    return frase