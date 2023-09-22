def uppCons(frase):
    '''função que recebe uma frase e a retorna com suas consoantes
    em maiúsculas'''
    contador = 0
    resultado = ''
    while contador < len(frase):
        if frase[contador] in 'bcdfghjklmnpqrstvxwyz':
            resultado = resultado + str.upper(frase[contador])
        else:
            resultado = resultado + frase[contador]
        contador = contador + 1
    return resultado