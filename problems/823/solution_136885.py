def faltante(lista):
    indice=0
    contador=0
   	if lista[0]!=1:
        return 1
	while contador<len(lista)-1:
        if lista[indice]+1==lista[indice+1]: