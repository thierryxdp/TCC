def uppCons(lista):
    i=0
    s=lista[0].upper()
    while i<len(s):
        if s[i] in 'AEIOUÃÉÍÓÚÊ':
            s=s.replace(s[i],s[i].lower())
            i+=1
        else:
            i+=1
    	return s