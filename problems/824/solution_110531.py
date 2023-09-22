def  uppCons(frase):
    '''Recebe uma frase e retorna todas suas consoantes em maiúsculas 
    sem modificar os caracteres restantes
    string-> string'''
    indice = 0
    nv_frase = ' ' 
    
    while indice < len(frase):
        if indice in 'BCDFGHJKLMNPQRSTVWYZVbcdfghjklmnpqrstvwyz':
            nv_frase = str.replace(frase, frase[indice], str.upper(frase[indice]))
        else:
            nv_frase =str.replace((frase, frase[indice],(frase[indice]))
    indice += 1
    return nv_frase