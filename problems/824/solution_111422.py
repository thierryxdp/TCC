def uppCons(frase):
    lista=[]
    listafrase = list(frase)
    frase1=('')
    vogais = ['a','e','i','o','u','A','E','I','O','U']
    i=0
    while i<len(listafrase[i]):
        if (listafrase[i] not in vogais)==True:
            C=list.append(lista,list.upper(frase[i]))
            escrita = str(C)
        elif (listafrase[i]in vogais)==True:
            k = (list.append(lista,frase[i]))
            escrita1 = str(k)
        i=i+1
            
    return (escrita + escrita1)