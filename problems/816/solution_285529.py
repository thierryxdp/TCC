def maiores(lista,n):
    '''retorna uma lista com todos os números da lista lista maiores que o número inteiro n
    	list,int->list'''
    
    lista_final=[]
    i=0
    
    if lista[i]>n:
        lista_final=lista_final + [lista[i]]
        i=i+1
    
    else:
        i=i+1
        
    return lista_final