def uppCons(frase):
    i=0
    NF=frase
    while i<len(frase):
        if frase[i] in 'qwrtypsdfghjklçzxcvbnm':
            NF = (str.replace(NF,NF[i],str.upper(NF[i]))
        i = i+1
    return NF