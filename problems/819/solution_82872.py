def filtraMultiplos(lista,num):
    """Essa funççao retorna todos os numeros multipos de
    um numero, dado uma lista de numeros
    lista,int->lista"""
    
    i=0
    lista_multiplos=[]
    
    while i<len(lista):
        
        if lista[i]%num==0:
            
            lista_multiplos = [lista[i]]
        
        i = i +1
        
        
        
	return lista_multiplos