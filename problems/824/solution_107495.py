def uppCons(frase):
    '''Retorna a frase com todas as consoantes
    em caixa alta;
    string -> string'''
    resultado = ''
    for letra in frase:
        if letra in 'bcdfgjklmnpqrstvwxzhçy':
            resultado += letra.upper() 
        else:
            resultado += letra
    return resultado