def uppCons(frase):
    """Função que recebe como entrada uma frase e retorna
    a frase co mtodas as consoantes em maiúsculas (e os 
    demais caracteres exatamente como estavam na frase
    original.
    str->str"""
    i=0
    s=''
    while i<len(frase):
        if frase[i] in "bcçdfghjklmnpqrstvxwyz":
           s += frase[i].upper()
        else:
            s += frase[i]
        i=i+1
    return s