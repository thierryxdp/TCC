def faltante(lista):
    lista.sort()
    i=0
    s=range(1,len(lista)+2)
    while i<len(lista)+1:
        if s[i] in lista:
    		i+=1
    	return s[i]