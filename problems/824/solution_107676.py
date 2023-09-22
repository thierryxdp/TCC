def uppCons(frase):
    frase_Maiuscula = ''
    posicao = 0
    
    while posicao < len(frase):
        caracter = frase[posicao]
        if frase[posicao] in 'bcdfghjklmnpqstvwxyz':
            caracter = caracter.upper()
        frase_Maiuscula = frase_Maiuscula + caracter
        posicao = posicao + 1
    return frase_Maiuscula