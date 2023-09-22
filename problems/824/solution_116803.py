def uppCons(frase):
    indece=1
    L=''
    while indece<=len(frase):
        if frase[indece-1:indece] in 'bcçdfghjklmnpqrstvxwyz':
            L+= str.upper(frase[indece-1:indece])
        else:
            L+=frase[indece-1:indece]
        indece=indece+1
    return L