def uppCons(frase):
    final = ''
    for letra in frase:
        if letra in 'bcdfghjklmnpqrstvxwyzç':
            final += letra.upper() 
        else: 
            final += letra
    return final