def uppCons(string):
    x = 0
    i = 0
    lista = list(string)
    while len(lista) > x:
        if lista[i] in 'bcdfghjklmnpqrstvwxyz':
            lista[i].upper()
        x += 1
        i += 1
    return ','.join(lista)