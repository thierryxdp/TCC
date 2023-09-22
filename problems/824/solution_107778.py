def uppCons(frase):
    nf=frase
    i=0
    
    while i < len(frase):
        if frase[i] in 'qwrtypsdfghjklçzxcvbnm':
            nf = (str.replace(nf,nf[i],str.upper(nf[i])))
        i = i + 1
    return nf