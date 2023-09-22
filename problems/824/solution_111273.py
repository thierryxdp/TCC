def uppCons(frase):
    """Função que recebe uma frase e retorna a mesma em maiúscula
    str -> str"""
    i=0
    while i<len(frase):
        if frase[i]in 'bcdfghjklmnpqrstvxwyz':
            str.upper(frase[i])
        i=i+1
    return frase