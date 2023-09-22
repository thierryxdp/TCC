def total(lista,dic):
    '''funcao que retorna o valor total dos itens da lista que estejam disponiveis nesta loja list, dict -> float'''
    a = 0
 
    for elem in range(len(lista)):
        
        m = lista[elem]
        
        if m in dict.keys(dic):
            
            a = a + dict.get(dic,m)
          
 	return round(a,2)