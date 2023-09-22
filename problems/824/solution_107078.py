def uppCons(frase):
    '''Função que recebe uma frase e retorna a mesma frase com todas as
    consoantes maiusculas.str->str'''
    refrase=''
    for caractere in frase:
        if caractere in 'bcdfghjklmnpqrstvxwyz':
            refrase=refrase+caractere.upper()
        else:
            refrase=refrase+caractere
    return refrase