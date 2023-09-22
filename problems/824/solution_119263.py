def uppCons(frase):
    frase_final = ''
    for letra in frase:
        if letra in 'bcdfghjklmnpqrstvwxyz':
            frase_final += letra.upper()
        else:
            frase_final += letra