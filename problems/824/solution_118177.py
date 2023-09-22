def uppCons(texto):
    ''' função que receba uma frase e retorna a frase com todas as consoantes em maiúsculas
    str, list -> str
    '''
    lista_frase = list(texto)
    i = 0
    letra = []
    while i < len(lista_frase):
        if lista_frase[i] in 'bcdfghjklmnpqrstvxywz':
            letra(i, lista_frase[i].str.upper())
        else:
            letra(i, lista_frase[i])
            i = i + 1
    return ''.join(letra)