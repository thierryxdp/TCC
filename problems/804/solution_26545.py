def filtr_pares(tupla):
    '''funçao querecebe tupla com quatro elementos 
    e retorna umatupla contendo sos elementos pares deta'''
    pares = []
    for item in tupla:
        if(item % 2 == 0):
            pares.append(item)
 	return tuple(pares)