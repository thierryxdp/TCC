def uppCons(frase):
    '''funcao que dado uma frase ,retoenará a frase com todas as suas consoantes em maiscula
    e os caracteres como eram na frase original 
    str -> str'''
    frase2 = ''
    tamanho = 0 
    consoante = 'cdfghjjlmnpqrstvwxyyzç'
    while tamanho <len(frase):
        if frase[tamanho] in consoante:
            frase2 = frase2 + (str.upper(frase[tamanho]))
        else:
            frase2 +frase2 + frase[tamanho]
                tamanho = tamanho + 1
    return frase2