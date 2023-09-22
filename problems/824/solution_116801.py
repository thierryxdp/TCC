def uppCons(frase):
    indece=1
    while indece<=len(frase):
        if frase[indece-1:indece] in 'bcdfghklmnpqrstvxwyz':
            str.replace(frase,frase[indece-1:indece],str.upper(frase[indece-1:indece]))
        indece=indece+1
    return frase