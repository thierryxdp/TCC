def uppCons(frase):
    vogais = ['a','e','i','o','u','A','E','I','O','U']
    i=0
    while i<len(frase):
        if (frase[i] in vogais)==False:
            k=str.upper(frase[i])
        i=i+1
            
    return k