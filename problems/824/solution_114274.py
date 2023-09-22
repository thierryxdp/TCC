def uppCons(frase):
    """retorna a frase com todas as suas consoantes em maiúsculas; str -> str"""
    a='bcdfghjklmnopqrstvwxyz'
    b=0
    while b<len(frase):
        str.replace(frase,a[b],str.upper(a[b]))
        b=b+1
    return frase