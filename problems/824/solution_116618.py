def uppCons(frase):
    '''
    função que recebe como entrada uma frase e retorna
    a frase com todas as consoantes em maiúsculas
    '''
    contador = 0
    frase2 = ""
    while contador < len(frase):
        if frase[contador] in "qwrtypsfghjklçzxcvnmb":
            frase[contador] = upper.frase[contador]
        contador = contador + 1
       
                                    

    return frase2