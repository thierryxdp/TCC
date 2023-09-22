def total(l,d):
    '''funcao que retorna o valor total dos itens da lista que estejam disponiveis nesta loja list, dict -> float'''
    i = 0
 
    for elem in range(len(l)):
        
        m = l[elem]
        
        if m in dict.keys(d):
            
            i = i + dict.get(d,m)
            
  	return round(i,2)