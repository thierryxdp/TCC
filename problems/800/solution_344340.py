def total(l,d):
    '''funcao que retorna o valor total dos itens da lista que estejam disponiveis nesta loja list, dict -> float'''
    x = 0
 
    for elem in range(len(l)):
        
        m = l[elem]
        
        if m in dict.keys(d):
            
            x = x + dict.get(d,m)
            
 	return round(x,2)