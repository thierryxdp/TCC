def uppCons(frase):
    ''' ''' 
    i=0
    while i<len(frase):
    	if frase[i] in 'bcdfghjklmnpqrsvxywz':
            l=frase[i]
            maiusculo=str.upper(l)
            frase=str.replace(frase,l,maiusculo)
            i+=1
            return frase