def faltante(listaL):
    i=0
    if listaL[0]!=1:
        return 1
    while i<len(listaL):
       	if listaL[i]==listaL[i+1]+1