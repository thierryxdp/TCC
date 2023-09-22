def conta_frases(texto):
    """coment"""
    s0=texto
    s1=str.replace(s0,"!",".")
    s2=str.replace(s1,"?",".")
    s3=str.replace(s2,"...",".")
    return len(str.split(s3,". "))