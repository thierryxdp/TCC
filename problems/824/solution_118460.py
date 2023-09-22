def uppCons(frase):
    count = 0
    lista = list(frase)
    caracteres = len(lista)
    while count != caracteres:
        if lista[count] in 'bcdfghjklmnpqrstvxwyz':
            str.upper(lista[count])
        count = count + 1
    return str(lista)