def uppCons(frase):
    """Função que recebe uma frase e retorna a mesma com todas as consoantes em maiúscula. str -> str"""
    i = 0
    r = ""
    while i < len(frase):
        letra = str(frase[i])
        if letra in "bcdfghjklmnpqrstvwxyzçBCDFGHJKLMNPQRSTVWXYZÇ":
            r = r + str.upper(letra)
            i = i+1
        else:
            r = r + str(letra)
            i = i+1
    return r