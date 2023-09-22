def faltante(lista):
    i=0
    proximo=0
    while proximo<len(lista):
        if (lista[i]-lista[i+1]) != 1:
        	i=i+1
        proximo=proximo+1
    return lista[i]+1