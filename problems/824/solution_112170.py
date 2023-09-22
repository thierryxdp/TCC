def uppCons(frase):
    vogal=['a','e','i', 'o','u']
    nv_frase=''
    while len(nv_frase)!=len(frase):
        for i in range(len(frase)):
        	if frase[i] not in vogal:
            	nv_frase+=map(str.upper(),frase[i])
     
    return nv_frase