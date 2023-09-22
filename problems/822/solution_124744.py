def repetidos(lista):
	proximo=0
    contador=0
    while proximo!=len(lista)-1:
        repeticoes=list.count(lista,lista[proximo])
        if repeticoes>1:
        	contador=contador+1
    	proximo=proximo+1
    return contador