def uppCons(frase):
    frase_Maiuscula = " "
    posicao = 0 
    
    while posicao < len(frase):
        caracter = frase[posicao]
        if frase[posicao] in 'bcçdfghklmnpqrstvwxyz':
            caracter = caracter.upper()
        frase_Maiuscula = frase_Maiuscula + caracter
        posicao = posicao + 1 
    return frase_Maiuscula