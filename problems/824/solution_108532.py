def uppCons(s):
    """
    Retorna a string com as consoantes em maiusculo
    """
    i=0
    up=""
    while i<len(s):
        if s[i] in "bcçdfghjklmnpqrstvwxyz":
            up=up+str.upper(s[i])
        else:
            up=up+s[i]
        i=i+1
    return up