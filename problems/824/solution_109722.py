def uppCons(frase):
    texto= 
    for letra in frase:
        if letra == 'bcdfghjklmnpqrstvwxz':
            texto.append(frase.replace(letra,frase.upper(letra)))
    return texto