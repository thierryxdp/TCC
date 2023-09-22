def uppCons(frase):
	i=0
    ora=''
    while i<(len(frase)):
        if 'bcdfghjklmnpqrstvwxyz' in frase[i]:
        	ora=str.replace(frase[i],'bcdfghjklmnpqrstvwxyz','BCDFGHJKLMNPQRSTVWXYZ')
        i=i+1
    return ora