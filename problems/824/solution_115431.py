def uppCons(frase):
    """
    Retorna uma frase com as consoantes maiúsulas.
    str-> str
    """
def uppCons(frase):
    i=0
    cmasc=''
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvçwxyz':
            cmasc=cmasc+frase[i].upper()
        else:
            cmasc=cmasc+frase[i]
        i=i+1
    return cmasc