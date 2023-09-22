def uppCons(frase):
    cont=0
    while cont<len(frase):
        if frase[cont] in 'bcdfghjlmnpqrstvxz':
            upper(frase[cont])
        cont=cont +1
    return frase