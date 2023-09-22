def uppCons (frase):
    """recebe como entrada uma frase e retorna a frase com todas as suas consoantes emmmaiúsculas (e os demais caracteres exatamente como estavam na frase original)"""
    i=0
    while i<len(frase):
        if frase[i]  in 'bcdfghjklmnpqrstvwxyzç':
            frase=frase[:i]+str.upper(frase[i])+frase[i+1:]
        i=i+1
    return frase