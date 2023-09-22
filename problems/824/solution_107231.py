def uppCons(frase):
    '''Função que dado uma frase, retorna a frase com todas as suas consoantes em maiúsculas, e os demais caracteres como eram inicialmente''' 
    frase2 = ""
    tamanho = 0
    consoante = "qwrtypsdfghjklzxcvbnmç"
    while tamanho < len(frase):
        if frase[tamanho] in consoante:
            frase2 = frase2 + (str.upper(frase[tamanho]))
        else:
            frase2 = frase2 + frase[tamanho]
        tamanho = tamanho + 1
    return frase2