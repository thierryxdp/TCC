def uppCons (frase):
    '''função que recebe uma frase e a retorna com todas suas consoantes em maiúsculas, sem alterar os restantes dos
    caracteres.'''
    
    indice=0
    
    while indice<len(frase):
        if frase[indice] in 'bcdfghjklmnpqrstvwxyz':
            frase = str(frase[:indice]) + str(frase[indice].upper()) + str(frase[(indice+1):])
        indice = indice + 1
    return frase