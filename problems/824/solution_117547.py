def uppCons(frase):
	i=0
    ora=''
    while i<(len(frase)):
        if 'bcdfghjklmnpqrstvwxyz' in frase[i]:
        	str.replace(frase[i],'bcdfghjklmnpqrstvwxyz','BCDFGHJKLMNPQRSTVWXYZ')
        i=i+1
    return frase