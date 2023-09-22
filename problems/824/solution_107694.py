def uppCons(frase):
    """recebe uma frase e retorna a frase com suas consoantes em maiuscula; str->str"""
    fraseM = ''
    posicao = 0
    
    while posicao < len(frase):
        caracter = frase[posicao]
        if frase[posicao] in 'bcçdfghjklmnpqrstvwxyz':
            caracter = caracter.upper()
        fraseM = fraseM + caracter
        posicao = posicao + 1
    return fraseM