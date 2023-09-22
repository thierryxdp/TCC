def uppCons(frase):
    '''função que recebe uma frase e retorna a frase com todas as suas consoantes maiúsculas:str->str'''
    c = ''
    for caractere in frase :
        if caractere in 'bcçdfghjklmnpqrstvwxyz':
            c += caractere.upper()
        else:
            c += caractere 
    return c