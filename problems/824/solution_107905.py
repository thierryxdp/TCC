def uppCons(frase):
    """ Função que recebe uma frase e retorna a mesma frase com todas as consoantes em maiúsculas
    	str -> str
    """
    s = ""
    for caractere in frase:
        if caractere in "bcdfghjklmnpqrstvwxz":
            s += caractere.upper()
        else:
            s += caractere
    return s