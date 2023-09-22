def uppCons(frase):
    f=''
    i=0
    while i<len(frase):
        if frase[i] in 'aeiouAEIOU':
        	f+= frase[i]
        else:
            
            f+=frase[i].upper()
        i+=1
    return f