def  uppCons(frase):
    '''Recebe uma frase e retorna todas suas consoantes em maiúsculas 
    sem modificar os caracteres restantes
    string-> string'''
    indice = 0
    nv_frase = frase 
    
    while indice < len(frase):
        if nv_frase[indice] in 'BCDFGHJKLMNPQRSTVWYZVbcdfghjklmnpqrstvwyz':
            nv_frase = str.replace(nv_frase, nv_frase[indice], str.upper(nv_frase[indice]))
        indice += 1
    return nv_frase