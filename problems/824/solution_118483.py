def uppCons(frase):
    '''retorna a frase com todas as consoantes em maiusculo;
    entrada-> frase; str->str'''
    x = ''
    for elemento in frase:
        if elemento in 'çbcdfghjklmnpqrstvxwyz':
            x += elemento.upper() 
        else: 
            x += elemento
    return x