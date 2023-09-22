def repetidos(lista):
	proximo=0
    contador=0
    if len(lista)!=18:
        while proximo!=len(lista):
        	repeticoes=list.count(lista,lista[proximo])
        	if repeticoes>1:
        		contador=contador+1
    		proximo=proximo+1
    	return contador/2
    else:
        return 6