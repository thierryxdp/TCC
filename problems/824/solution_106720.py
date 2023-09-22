def uppCons(frase):
    """coment"""
    i=0
    while frase[i] in "AEIOUaeiou":
        str.upper(frase[i])
        i=i+1
    return frase