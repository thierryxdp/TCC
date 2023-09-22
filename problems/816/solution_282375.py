def maiores(x,y):
    '''A função retorna todos os números maiores que 
    o parâmetro y na lista x
    lista -> lista'''
    
    
    i = 0
    u = []
    
    while len(x) >i:
        if y > x[i]:
            list.append(u, x[i])
        i = i + 1
        
    list.sort(u)
    
    return u