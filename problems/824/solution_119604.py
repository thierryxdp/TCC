def uppCons(frase):
    """Função que recebe como entrada uma frase e retorne a 
    frase com todas as suas consoantes em maiúsculas
    Assinatura: str -> str"""
    i = 0
    while i<len(frase):
        if frase[i]in "bcdfghjklmnpqrstvxwyz":
            str.upper(frase[i])
            i = i + 1
            return frase