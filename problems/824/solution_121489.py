def uppCons(frase):
    m=""
    for letra in frase:
        if letra in "bcdfghjklmnpqrstvwxyzç":
            m=m+letra.upper()
        else:
             m=m+letra
    return m