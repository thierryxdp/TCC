def faltante(lista):
    '''Entre com uma lista para ser retornado o valor que esta faltando
    Lista -> Int'''
	i=0
    tam=(len(lista))+1
    num=0
    
    while i<tam:
        if lista[i]!=i:
            num=i
            return num
        i=i+1
    return [-1]