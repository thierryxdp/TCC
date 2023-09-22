def faltante(lista):
    '''Entre com uma lista para ser retornado o valor que esta faltando
    Lista -> Int'''
    Nlista=lista
    Nlista.sort()
    i=lista[0]
    x=(len(lista))+1
	
    while i<=x:
        if lista[i]!=i:
            maior=maior+lista[i]
        i=i+1
        
    return Nlista