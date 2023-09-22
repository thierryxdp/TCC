def uppCons(frase):
	i=0
    ora=''
    while i<(len(frase)):
        if 'aeiouAEIOU' not in frase[i]:
         str.upper(frase[i])
       		ora=ora+str(frase[i])
       	i=i+1
    return ora