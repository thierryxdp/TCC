def uppCons(frase):
	i=0
    ora=''
    while i<(len(frase)):
        if 'aeiouAEIOU' not in frase[i]:
         str.upper(frase[i])
        i=i+1
       	ora=ora+str(frase[i])
    return ora