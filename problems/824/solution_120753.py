def uppCons(frase):
    fraseNova=''
    i=0
    
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvxwyz':
            fraseNova=fraseNova+str.upper(frase,frase[i])
            i=i+1
            return frase