def uppCons(frase):
    '''função que recebe uma frase e retorna a mesma frase
    com as consoantes em maiúsculo
    str -> str
    '''
    cons_up = ''
    indice = 0
    while indice < len(frase):
        if frase[indice] in 'bcçdfghjklmnpqrstvwxyz':
            cons_up += frase[indice].upper()
        else:
            cons_up += frase[indice]
        indice += 1
    return cons_up