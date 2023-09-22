def uppCons(frase):
    i=0
    cont = ''
    while i<len(frase):
        if frase[i]in 'bcdfghjklmnpqrstvxwyz':
            letra = str.upper(frase[i])
            cont = cont + letra
            i=i+1        
        else:
            cont += letra
            return cont