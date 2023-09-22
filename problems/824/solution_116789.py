def uppCons(frase):
    '''
       Funcao que recebe uma frase de entrada e a retorna
       com todas as suas consoantes em letra maiusculas
       str -> str
    '''
    f = 0
    letras = []
    frase2 = list(frase)

    while f < len(frase2):
        if frase2[f] in 'bcdfghjklmnpqrstvwxyz':
            letras.insert(f,frase2[f].upper())
            f += 1
        else:
            f += 1

    return ''.join(letras)