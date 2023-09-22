def uppCons(frase):
    '''função que recebe uma frase e a retorna com suas consoantes
    em maiúsculas'''
    contador = 0
    while contador < len(frase):
        if frase[contador] in 'bcdfghjklmnpqrstvxwyz':
            str.upper(frase[contador])
        contador = contador + 1
    return frase