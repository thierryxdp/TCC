def uppCons(frase):
    i=0
    resposta=''
    while i<len(frase):
        if frase[i] not in 'AEIOUaeiou':
            resposta+=str.upper(frase[i])
        else:
            resposta+=frase[i]
    	i=i+1
    return resposta