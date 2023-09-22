def filtraMultiplos(lista,num):
    i=0
    result=[]
    while i <= len(lista):
    	if (lista[i]%num == 0):
            divisivel = lista[i]
    		result.append(divisivel)
    i+=1
            
    return result