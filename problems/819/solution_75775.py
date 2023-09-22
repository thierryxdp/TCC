def filtraMultiplos(lista,n):
    lista_div=[]
    proximo=0
    while proximo<len(lista):
   		if lista[proximo]%n==0:
            lista_div.append(lista[proximo]) 
       	proximo=proximo+1
    return lista_div