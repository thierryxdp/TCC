def faltante(lista:list)->int:
    '''retorna qual número está faltando na lista'''
    
    i=0
    while 1 < len(lista):
        if lista[i] -1 not in lista and lista[i] -1 !=0:
            return lista[i] -1
        i +=1
	returnlista[-1]+1