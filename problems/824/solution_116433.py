def uppCons(frase):
    t=0
    frase2=''
    while t< len(frase):
        if frase[t] not in 'AEIOUaeiouÁÉÍÓÚáéíóúÃÕãõ':
            frase2=frase2+str.upper(frase[t])
            t=t+1
        elif t< len(frase):
            frase[t] in 'AEIOUaeiouÁÉÍÓÚáéíóúÃÕãõ'
            frase2=frase2+frase[t]
            t=t+1
    return frase2