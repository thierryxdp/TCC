def uppCons(texto):
    i=0 
    while i<len(texto):
        letra=texto[i]
        novotexto=texto
        if letra.lower() in 'bcdfghjklmnpqrstvwxyzç':
            letra = str.upper(letra)
            novotexto+=letra
        i=i+1
    return novotexto