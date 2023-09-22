def uppCons(frase):
    """
    	Funcao que recebe uma frase.
        Retorna a frase recebido com todos as consoantes em maiúsculas;
        str -> str
    """
    frase_modificada = ""
    consoantes = "bcdfghjklmnpqrstvwxyzç"
    for caracter in frase:
        if caracter in consoantes:
       		caracter = caracter.upper()
        frase_modificada += caracter
    return frase_modificada