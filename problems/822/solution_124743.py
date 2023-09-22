def repetidos(lista):
	proximo=0
    contador=0
    repeticoes=list.count(lista,lista[proximo])
    while proximo!=len(lista)-1:
        if repeticoes>1:
        	contador=contador+1
    	proximo=proximo+1
    return contador