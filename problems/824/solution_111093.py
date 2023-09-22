def uppCons(frase):
    i=0
    s=''
    
    frase.split()
    while i < len(frase):
        if frase[i] in 'kkdjdhdhdjdjw':
            s=s+str.upper(frase[i])
            i=i+1
    return s