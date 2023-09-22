def consoantes_maiusculas(frase):
    '''Função que recebe string e devolve 
    ela com todas as suas consoantes em maiusculo
    str->str'''
    s = ''
    for caractere in frase:
        if caractere in 'bcdfghjklmnpqrstvxwyz':
            s += caractere.upper()
        else:
            s += caractere
    return s