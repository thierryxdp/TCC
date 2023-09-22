def listinha(lista):
	posfinal = len(lista-1)
    elmfinal = lista[posfinal]
    final =[]
    contador = 0
    
    while elmfinal+contador>0:
        final += [elmfinal-contador]
        contador-= 1
    return posfinal

def faltante(lista):
    #formato [1,n]
    contador =0
    faltante = []