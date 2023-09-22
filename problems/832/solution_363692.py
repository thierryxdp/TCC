def eh_quadrada(m):
    '''
       Função que retorna um booleano mostrando se a matriz
       é quadrada ou não
       list->booleano
    '''
    
    final=0

    for i in m:
        if len(i)==len(m):
            final+=1
            
            return True
    
        else:
            return False
        
    if len(m)==0:
            
        return True