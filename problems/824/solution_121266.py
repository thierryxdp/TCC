def uppCons(frase):
    vogais=['a','e','i','o','u','A','E','I','O','U','ã','ó','ú','í']
    i=0
    while i<len(frase):
        if frase[i] not in vogais:
            frase=str.replace(frase,frase[i],str.upper(frase[i]))
        i=i+1
    return frase