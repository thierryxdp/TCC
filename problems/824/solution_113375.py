def uppCons(frase):
    ''''''
    i=0
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyzç':
            substituir=str.replace(frase,frase[i],str.upper(frase[i]))
            frase= substituir
    	i=i+1
return frase