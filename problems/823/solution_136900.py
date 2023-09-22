def faltante(lista):
    indice=0
    cont=0
    if lista[0]!=1:
        return 1
    while cont<len(lista)-1:
        if lista[indice]+1==lista[indice+1]:
            indice=indice+1
            cont=cont+1
      	else:
            cont=len(lista)
   	return lista[indice]+1