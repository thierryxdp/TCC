def uppCons(frase):
    indece=1
    while indece<=len(frase):
        if frase[0:indece] in 'bcdfghjklmnpqrstvxwyz':
            str.replace(frase,frase[0:indece],str.upper(frase[0:indece]))
    indece=indece+1
    return frase