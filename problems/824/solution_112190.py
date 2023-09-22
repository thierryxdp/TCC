def uppCons(frase):
    vogal=['a','e','i', 'o','u','ã','ú']
    nv_frase=[]
    for i in range(len(frase)):     
        if frase[i] not in vogal:
            letra=list(map(str.upper,frase[i]))
            nv_frase+=letra
        else:
            nv_frase+=frase[i]  
    nv_frase=''.join(map(str, nv_frase))
    return nv_frase