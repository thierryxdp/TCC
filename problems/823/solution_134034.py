def faltante(lista):
    '''
    '''
    contador = 0
    while contador<len(lista):
       	if contador != (lista[contador-1])+1:
            return (lista[contador-1])+1
     	contador += 1