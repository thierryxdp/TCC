def faltante(lista):
    i=0
    s=range(1,len(lista)+2)
    while i<len(lista):
        if s[i] in lista:
    		i+=1
    		return s[i]