def uppCons(frase): #REVISAR - RETORNA APENAS A ULTIMA CONSOANTE

    indice = 0
    
    while indice < len(frase):
        if frase[indice] in 'bcdfghjklmnpqrstvwxyz':
           str.replace(frase,frase[indice],str.upper(frase[indice]))
        indice += 1
    return frase