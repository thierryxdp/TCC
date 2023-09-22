def uppCons1 (frase):
    '''Funcao que, dada uma frase, retorna a mesma frase com todas as consoantes maiusculas.
    str->str'''
    
    i=0
    frase_alterada = ''
    while i<len(frase):
        caracter = frase[i]
        if frase[i] in 'bcdfghjklmnpqrstvxwyz':
            caracter = str.upper(caracter)
        frase_alterada=frase_alterada + caracter
        i=i+1
    return frase_alterada