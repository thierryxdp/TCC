def busca(m, setor):
    '''
    dada uma matriz de informações, retorna, a partir do setor, informações dos funcionários
    list, str -> tuple
    '''
    nlin = len(m)
    ncol = len(m[i])
    resposta=[]
    for i in range(nlin):
        for el in range(ncol):
            if m[i][2] == setor:
                resposta = resposta + [m[i][0],[mi][1),m[i][3]]
            else:
                resposta = []
    return resposta
    
                                    
                                   
                                       
                                       
                                       
                
        
    
    

    
    
    
    
    nlin = len(m)
    ncol = len(m[0])
    qtd_elem = 0
    vazia=[]
    for i in range(nlin):
        for el in range(ncol):
            if m[i][el] == n:
                qtd_elem = qtd_elem + 1
            elif m=vazia:
                qtd_elem = 0
    return qtd_elem