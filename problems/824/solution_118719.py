def uppCons(frase):
    """Função que, dada uma frase, retorna a frase com todas
    as suas consoantes em maiúsculas (e os demais caracteres
    exatamente como estavam na frase original).
    str -> str"""
    i = 0
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyzç':
            frase = frase[:i] + str.upper(frase[i]) + frase[i+1:]
        i = i + 1
    return frase