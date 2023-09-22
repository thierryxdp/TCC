def filtra_pares(s):
    """função que recebe uma tupla e retorna uma nova tupla contendo apenas
    pares da tupla original, na mesma ordem em que se encontraval
    tupla-> tupla"""
    a,b,c,d=s
    a= s[0]
    b=s[1]
    c=s[2]
    d=s[3]
    if a%2==0:
        return s=s+(a,)
        if b%2==0:
            return s=s+(b,)
            if c%2==0:
                return s=s+(c,)
                if d%2==0:
                    s=s+(d,)
                    return s
                else:
                    return s[0],s[1],s[2]