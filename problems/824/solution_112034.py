def uppCons(string):
    ''''''
    contador = 0
    acumulador = ''
    consoantes = 'bcçdfghjklmnpqrstvwxyz'
    while contador < len(string):
        if string[contador] in consoantes:
            acumulador = acumulador + str.upper(string[contador])
        else:
            acumulador = acumulador + string[contador]
        contador = contador + 1
    return acumulador