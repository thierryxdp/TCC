def uppCons(frase):
    '''função que recebe como entrada uma frase e retorna a frase com todas as suas consoantes em maiúsculas str->str'''
    return ''.join(caractere.upper() if caractere in 'bcçdfghjklmnpqrstvxwyz' else caractere for caractere in frase)