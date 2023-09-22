def uppCons(frase):
    '''
    função que recebe como entrada uma frase e retorna
    a frase com todas as consoantes em maiúsculas
    '''
    contador = 0
    frase2 = ""
    letra=frase[contador]    
    while contador < len(frase):
        if letra in "qwrtypsfghjklçzxcvnmb":
            letra = letra.upper
        contador = contador + 1
       
                                    

    return frase