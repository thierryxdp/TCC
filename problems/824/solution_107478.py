def uppCons(frase):
    '''
    A função retorna todas as consoantes
    em maiusculo.
    string -> string
    '''
    i = 0
    frase_list = list(frase)
    while i < len(frase_list):
        if frase_list[i] in 'bcdfghjklmnpqrstvxwyz':
            frase_list[i] = frase_list[i].upper()
        else:
            frase_list[i] = frase_list[i]
        i = i+1
    return ''.join(frase_list)