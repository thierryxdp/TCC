def uppCons(texto):
    i=0 
    letra=texto[i]
    while i<len(texto):
        if letra.lower() in 'bcdfghjklmnpqrstvwxyzç':
            letra = str.upper(letra)
        i=i+1
    return texto