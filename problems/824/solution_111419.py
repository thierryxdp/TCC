def uppCons(frase):
    lista=[]
    listafrase = list(frase)
    frase1=('')
    vogais = ['a','e','i','o','u','A','E','I','O','U']
    i=0
    while i<len(listafrase[i]):
        if (listafrase[i] not in vogais)==True:
            C=(str.append(lista[],str.upper(frase[i])))
        elif (listafrase[i]in vogais)==True:
            k = (str.append(lista[],frase[i]))
        i=i+1
            
    return (C + k)