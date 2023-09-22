def maiores(lista,n):
    '''função que retorna uma lista com todos os numeros maiores do que o n da liata dada;
    list -> list'''
    
    if lista[0] > n:
        l1 = lista[0]
    
    elif lista[1] > n:
        l2 = lista[1]
    
    elif lista[2] > n:
        l3 = lista[2]
    
    elif lista[3] > n:
        l4 = lista[3]
    
    elif lista[4] > n:
        l5 = lista[4]
        
    lista = [l1,l2,l3,l4,l5]        
    return lista