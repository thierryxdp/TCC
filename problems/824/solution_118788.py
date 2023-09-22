def uppCons(frase):
    '''
    Dado uma frase modifica todos as consoantes minisculas 
    para maisculas
    str->str
    '''
    x = 0
    f = []
    while x < len(frase):
        if str.lower(frase[x]) in "bcdfghjklmnpqrstvxywzç":
            list.append(f, str.upper(frase[x]))
        else:
            list.append(f, frase[x])
        x = x + 1
    return str.join("", f)