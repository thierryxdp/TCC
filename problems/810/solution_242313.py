def inverte (frase):
    '''
    	essa função recebe uma frase como entrada e a retorna inversa, 
        sem letras maiusculas e sem pontuação
        str->str
    '''
    for x in "?!.,;:":
        frase = frase.replace(x, "")
    return frase.upper()