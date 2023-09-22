def lingua_p(palavra):
    '''
    Função que recebe uma palavra e retorna a mesma palavra
    traduzida para a língua do P.
    
    str -> str
    '''
    a = ""
    for letra in palavra:
        if letra.lower() in "aáéeiouú":
            a = a + letra + "p" + letra
        else:
            a = a + letra
    return a.lower()