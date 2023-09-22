def uppCons(frase):
    contador = 0
    teste = ''
    while contador<len(frase):
        if frase in 'bcdfghjklmnpqrstvwxyz':
            teste += caractere.upper()
        else:
            teste += frase
        contador = contador + 1
    return teste