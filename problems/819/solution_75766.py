def filtraMultiplos(lista,n):
    lista_div=[]
    proximo=0
    while proximo<len(lista):
   		if lista[proximo]/n:
            lista_div=lista_div+[lista[proximo]]
    proximo=proximo+1
    return lista_div