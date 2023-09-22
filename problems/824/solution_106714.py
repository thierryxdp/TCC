def uppCons(frase):
    """dada uma frase, retorna a frase com todas as suas consoantes em maiúsculas, mantendo os demais caracteres 
    exatamente como estavam na frase original; str -> str"""
    i = 0
    frase_maiuscula = ''
    while i < len(frase):
        if frase[i] in 'bcçdfghjklmnpqrstvwxz':
            frase_maiuscula = frase_maiuscula + str.upper(frase[i])
        else:
            frase_maiuscula = frase_maiuscula + frase[i]
        i = i + 1
    return frase_maiuscula