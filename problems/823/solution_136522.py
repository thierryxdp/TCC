def listinha(lista):
	posfinal = len(lista)-1
    elmfinal = lista[posfinal]
    final =[]
    contador = 0
    
    while elmfinal+contador>0:
        final += [elmfinal+contador]
        contador-= 1
    	list.sort(final)

def faltante(lista):
    contador = 0
    faltante = 0
    while contador<len(lista):
        if lista[contador] not in listinha(lista):
        	faltante+= lista[contador]
        	contador+=1
        else:
            contador +=1
            
            
  	return faltante