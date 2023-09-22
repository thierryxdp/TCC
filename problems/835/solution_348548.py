def melhor_volta(matriz) : 
    """Analisa uma matriz dada, a qual indica o tempo de 
    cada volta de cada corredor. Dessa forma, retorna uma
    tupla com as informações do corredor com a melhor volta 
    da prova, informando também o tempo e o número da volta
    respectivo; 
    list -> tupla"""
    
    a = []  #melhor_volta_de_cada_corredor_em_ordem
    d = []  #lista com tuplas_corredor_melhortempo_volta
    corredor = 1 
    
    for x in matriz :
        volta = 0
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
    z = 0 
    for m in a : 
        
        if min(a) == m :
            z = quantidade 
        quantidade = quantidade + 1 
     
        
    return d[z]