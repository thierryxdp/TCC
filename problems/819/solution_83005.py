def filtraMultiplos(lista_num,n):
    '''analisa e retorna uma lista apenas com os números da lista lista_num que são divisíveis por n
    	list,int->list'''
    
    lista_final=[]
    i=0
    
    while i<len(lista_num):
        if lista_num[i]%n==0:
            
        	lista_final.append(lista_num[i])
        
    return lista_final