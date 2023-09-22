def uppCons(frase):
    texto=''
    i=0
    
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvxwyz':
            texto=texto+str.upper(frase,frase[i])
            i=i+1
            return texto