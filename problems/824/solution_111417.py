def uppCons(frase):
    frase1=('')
    vogais = ['a','e','i','o','u','A','E','I','O','U']
    i=0
    while i<len(frase):
        if (frase[i] not in vogais)==True:
            C=(str.append(frase1,str.upper(frase[i])))
        elif (frase[i] in vogais)==True:
            k = (str.append(frase1,frase[i]))
        i=i+1
            
    return (C + k)