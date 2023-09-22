def uppCons(texto):
    i=0 
    while i<len(texto):
        letra=texto[i]
        i=i+1
        if letra.lower() in 'bcdfghjklmnpqrstvwxyzç':
            letra = str.upper(letra)
    return texto