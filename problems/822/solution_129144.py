def repetidos(numeros):
    i=+1
    rep=0
    while i<len(numeros)-1:
        if numeros[i]==numeros[i+1]:
         		rep=rep+1
    	i=i+1
    return rep