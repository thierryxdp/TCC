def uppCons(frase):
    '''Recebe como entrada uma frase e retorna
    a frase com todas as consoantes em maisculas.
    string -> string'''
    while 'aeiou' not in frase:
        palavra = frase.upper()
        return palavra