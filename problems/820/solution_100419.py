def posLetra (frase,letra,n):
    i=0
    lista=[]
    if str.count(frase,letra)<n:
        return -1
    else:
        while i<len(frase):
        	if frase[i]==letra:
            	lista=lista+[str.index(frase,letra,i)]
       		i=i+1
        return list.pop(lista,n-1)