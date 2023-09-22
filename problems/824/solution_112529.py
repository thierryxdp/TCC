def uppCons(frase):
    i=0
    while i<len(frase):
        if frase[i] in 'qwrtypsdfghjklçzxcvbnm':
            str.upper(frase[i])
        i=i+1
        frase=''.join(c.upper() if c in 'qwrtypsdfghjklçzxcvbnm' else c for c in frase
        return frase