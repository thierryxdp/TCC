def lingua_p(frase):
    """str -> str"""
    """retorna a frase em português na língua do p"""
    
    str.lower(frase)
    F = ""
    p = "p"
    
    for l in frase:
        if l in "aeiouáâãéêíóôõú":
            F += l + p + l
            pass
        else:
            F += l
        pass
    return F