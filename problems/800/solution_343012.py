def total(lista,produtos):
    '''analisa e retorna o preço da lista de compras de acordo com o preço dos produtos
    	list,dict->float'''
    
    i=0
    
    for j in range(len(lista)):
        
        if lista[j] in produtos:
            
            i=i+produtos.get(lista[j])
            
    return round(i,2)