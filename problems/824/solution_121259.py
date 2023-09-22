def uppCons(frase):
    vogais=['a','e','i','o','u','A','E','I','O','U']
    while i<len(frase):
        if frase[i] not in vogais:
            str.replace(frase,frase[i],str.upper(frase[i]))
        i=i+1
    return frase