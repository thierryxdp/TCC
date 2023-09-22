def uppCons(frase):
    '''
    função que recebe como entrada uma frase e retorna
    a frase com todas as consoantes em maiúsculas
    '''
    contador = 0
    frase2 = ""
       
    while contador < len(frase):
        letra=frase[contador]  
        if letra in "qdwrtypsfghjklçzxcvnmb":
            frase2 = frase2 + letra.upper()
        else:
            frase2 = frase2 + letra
        contador = contador + 1 
    return frase2