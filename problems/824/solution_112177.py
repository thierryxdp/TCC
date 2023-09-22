def uppCons(frase):
    vogal=['a','e','i', 'o','u']
    nv_frase=''
    while len(nv_frase)!=len(frase):
        for i in range(len(frase)):
        	if frase[i] not in vogal:
            	letra=str(map(str.upper(frase),frase[i]))
                nv_frase+=letra
    return nv_frase