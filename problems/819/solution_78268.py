def filtraMultiplos(lista,numero):
    '''funcao que retorna uma lista com os multiplos de `numero` que estao na lista dada;list,int-->list'''
    i=0
    x=[]
    while i< len(lista):
    	if lista[i]%numero==0:        
    		z=lista[i]
        	list.append(x,z)
        i=i+1
    return x