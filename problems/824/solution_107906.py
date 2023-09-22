def uppCons(frase):
    """ Função que recebe uma frase e retorna a mesma frase com todas as consoantes em maiúsculas
    	str -> str
    """
    s = ""
    for caractere in frase:
        if caractere in "bcdfghjklmnpqrstvwxzç":
            s += caractere.upper()
        else:
            s += caractere
    return s