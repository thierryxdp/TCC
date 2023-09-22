def uppCons(frase):
    frase_alterada = ''
    i = 0
    while i <len(frase):
        if frase[i] not in 'AEIOUaeiou':
            frase_alterada = frase_alterada + str.replace(frase,frase[i],str.upper(frase[i]))
        i= i+1
    return frase_alterada