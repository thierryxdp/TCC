def uppCons(f):
    """recebe como entrada uma frase e retorna a frase com todas as suas
    consoantes em maisculas"""
    n=0
    
    while n<len(f):
        if not 'a' or 'e' or'i' or'o' or'u' in f[n]:
            str.upper(f[n])
        n+=1
    return f