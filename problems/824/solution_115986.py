def uppCons(frase):
    '''Esta e a funcao que recebe como entrada uma 
    frase e retorna a frase com todas as consoantes 
    em maiusculas'''
    s = ''
    consoantes = 'bcçdfghjklmnpqrstvxwyz'
    for caractere in frase:
        if caractere in consoantes:
            s=s+caractere.upper()
        else:
            s=s+caractere
    return s