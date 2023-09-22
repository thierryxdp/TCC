def faltante(lista):
    padrao = list(range(1,len(lista)+2,1))
    i=0
    
    while i<=len(padrao):
    	if padrao[i] not in lista:
            return i+1
        i= i +1