def total(L,D):
    '''funcao que retorna o valor total dos itens da lista que estejam disponiveis nesta loja list, dict -> float'''
    i = 0
    
    for elem in range(len(L)):
        
        m = L[elem]
        
        if m in dict.keys(D):
            
            i = i + dict.get(D,m)
            
  	return round(i,2)