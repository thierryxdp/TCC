def uppCons(texto):
    i=0 
    while i<len(texto):
        letra=texto[i]
        novotexto+=letra
        
        if letra.lower() in 'bcdfghjklmnpqrstvwxyzç':
            letra = str.upper(letra)
            
        i=i+1
    return novotexto