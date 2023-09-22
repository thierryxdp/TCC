def uppCons(frase):
    vogal=['a','e','i', 'o','u']
    for i in range(len(frase)):
        nv_frase=[]
        if frase[i] not in vogal:
            letra=list(map(str.upper,frase[i]))
            nv_frase+=letra
        else:
            nv_frase+=frase[i]  
    return nv_frase