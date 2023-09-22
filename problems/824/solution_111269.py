def uppCons(frase):
    """Função que recebe uma frase e retorna a mesma em maiúscula
    str -> str"""
    c = 0
    consoante = ''
    while c <= len(frase):
        if frase[c] in 'BCDFGHJKLMNPQRSTUVWXYZbcdfhjklmnpqrstuvwxyz'
        consoante = frase[c]
        
        c+= 1
    return frase == str.upper