def uppCons(frase):
    """
    	Funcao que recebe uma frase.
        Retorna a frase recebido com todos as consoantes em maiúsculas;
        str -> str
    """
    consoantes = "bcdfghjklmnpqrstvwxyz"
    for caracter in frase:
        if caracter in consoantes:
       		caracter = caracter.upper()
            
    return frase