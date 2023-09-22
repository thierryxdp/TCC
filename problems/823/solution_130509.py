def faltante(lista):
    padrao = list(range(1,n+1,1))
    i=0
    
    while i<len(padrao):
    	if padrao[i] not in lista:
            return i
        i= i +1