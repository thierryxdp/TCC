def uppCons(frase):
    '''Retorna uma frase com todas as consoantes em maiúsculas
    string -> string '''
    i = 0
    frase2 = []
    while i < len(frase):
        if str.lower(frase[i]) in 'bcdfghjklmnpqrstvwyxzç':
            list.append(frase2, str.upper(frase[i]))
        else:
         	list.append(frase2, frase[i])
        i = i + 1
    return str.join('', frase2)