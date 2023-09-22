def uppCons(texto):
    i=0 
    novotexto=''
    while i<len(texto):
        letra=texto[i]
        
        if letra.lower() in 'bcdfghjklmnpqrstvwxyzç':
            letra = str.upper(letra)
        
        novotexto+=letra
        i=i+1
    return novotexto