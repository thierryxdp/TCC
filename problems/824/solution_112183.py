def uppCons(frase):
    for i in range(len(frase)):
        vogal=['a','e','i', 'o','u']
        nv_frase=[]
        if frase[i] not in vogal:
            letra=list(map(str.upper,frase[i]))
            nv_frase+=letra
        else:
            nv_frase+=frase[i]
        
    return nv_frase