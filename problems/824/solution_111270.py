def uppCons(frase):
    """Função que recebe uma frase e retorna a mesma em maiúscula
    str -> str"""
   s = ''
    while caractere in frase:
        if caractere in 'bcdfghjklmnpqrstvxwyz':
            s += caractere.upper() 
        else: 
            s += caractere
    return s