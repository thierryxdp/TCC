def uppCons(frase):
    ''' função que recebe uma frase como entrada e retorna
    	todas as consoantes em maiúsculo.
        str ---> str'''
    a = 0
    frase_final = ' '
    while a < len(frase):
        if frase[a] in 'bcdfghjklmnpqrstvwxyz':
            frase_final = frase_final + frase[a]
            a += 1
        return frase_final