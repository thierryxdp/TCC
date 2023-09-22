def faltante(lista):
    i=0
    s=range(1,len(lista)+2)
	while True:
        if i+1==s[i]:
            return i+1
        i+=1