def uppCons(frase):
    """Retorna a frase com todas as suas consoantes em maiúsculas (e os demais caracteres exatamente como estavam na frase original)"""
    """str -> str"""
    i = 0
    frasenova = ""
    
    while (i < len(frase)):
        if (str.lower(frase[i]) in "bcdfghjklmnpqrstvwxz" :
            frasenova += str.upper(frase[i])
        else:
            frasenova += frase[i]
            
        i = i + 1
    return frasenova