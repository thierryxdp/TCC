def uppCons(frase):
    vogal=['a','e','i', 'o','u']
   	nv_frase=[]
    for i in range(len(frase)):     
        if frase[i] not in vogal:
            letra=list(map(str.upper,frase[i]))
            nv_frase+=letra
        else:
            nv_frase+=frase[i]  
    return nv_frase