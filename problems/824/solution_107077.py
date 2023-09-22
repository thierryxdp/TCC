def uppCons(frase):
    '''Função que recebe uma frase e retorna a mesma frase com todas as
    consoantes maiusculas.str->str'''
    refrase=''
    i=0
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvxwyz':
            refrase=refrase+str.upper(frase[i])
        else:
            refrase=refrase+frase[i]
    return refrase