def uppCons(frase):
    frase_alterada = frase
    i = 0
    while i <len(frase):
        if frase[i] not in 'AEIOUaeiou':
            frase_alterada = str.replace(frase_alterada,frase[i],str.upper(frase[i]))
        i= i+1
    return frase_alterada