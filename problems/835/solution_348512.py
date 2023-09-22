def melhor_volta(matriz) : 
    """Determina """
    
    a = []  #melhor_volta_de_cada_corredor_em_ordem
    d = []  #indicação_corredor_e_volta
    corredor = 1 
    volta = 0
    for x in matriz :
        b = [] 
        for y in x :
            list.append(b,y) 
            
        c = min(b)
        
        Ind = 0
        for indice in b :
            
            if indice == c :
                volta = Ind
            Ind = Ind + 1 
            
        list.append(d,(corredor,c,volta+1)) 
        list.append(a,c)
        corredor = corredor + 1
      
    quantidade = 0 
    for m in a : 
        
        if min(a) == m :
            x = quantidade 
        quantidade = quantidade + 1 
     
        
    return d[quantidade]