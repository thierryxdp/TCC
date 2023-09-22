def repetidos(numeros):
    cont=+1
    rep=0
    while cont<len(numeros)-1:
        if numeros[cont]==numeros[cont+1]:
         		rep=rep+1
    	cont=cont+1
    return rep