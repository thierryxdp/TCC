def filtraMultiplos(lista,n):
	    '''' '''
	    lista_nova= []
	    indice=0  
	    while indice <= len(lista):
	        if lista[indice]%n !=0:
	            indice +=1
	        if lista[indice]%n ==0:
	            lista_nova.append(lista[indice])
	            indice +=1
	        if indice > len(lista):
            	break
	    return lista_nova