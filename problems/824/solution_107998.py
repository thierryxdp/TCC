def uppCons (frase):
    '''Funcao que, dada uma frase, retorna a mesma frase com todas as consoantes maiusculas.
    str->str'''
    
    frase_alterada = ''
    i=0
    while i<len(frase):
        caracter = frase[i]
        if caracter in 'bcdfghjklmnpqrstvxwyz':
            caracter = str.upper(caracter)
            frase_alterada = frase_alterada + caracter
        i=i+1
    return frase_alterada + caracter