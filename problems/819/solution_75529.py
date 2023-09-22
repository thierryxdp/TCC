def filtraMultiplos(lista,numero):
    indice=0
    proximo=0
    lista2=[]
    divisor=(lista[indice]%numero)
    while proximo<len(lista):
        if divisor==0:
    		indice=indice+1
    		proximo=proximo +1
    		lista2=lista2+lista[indice]
    return lista2