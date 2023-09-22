def falante(lista):
    '''
    '''
    contador = 0
    while contador<len(lista):
       	if contador != (contador-1)+1:
            return (contador-1)+1
		contador +=1