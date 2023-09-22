def faltante(listaL):
    listaL.sort()
    numList=list(range(1, max(listaL)+1))
    i=0
    i2=0
    miss=0
    while i2 < len(listaL):
    	if listaL[i2]!=numList[i]:
   			miss=numList[i]
        i+=1
   	 	i2+=1
    return miss