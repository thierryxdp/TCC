def pontos_por_time(lista):
    ''' funcao que atraves de uma lista que contem dois elementos que sao uma lista retorna um dicionario cujos mapeamentos são nome do time e numero total de pontos
        list[list[str,str,list[int,int], list[str,str,list[int.int]]] '''
    
    if lista[0][2][0] == lista[0][2][1]:
        
        if lista [1][2][0] == lista [1][2][1]:
            return {lista[0][0]:2, lista[0][1]:2}
        
        elif lista [1][2][0] > lista [1][2][1]:
            return {lista[0][0]:1, lista[0][1]:4}
        
        elif lista [1][2][0] < lista [1][2][1]:
            return {lista[0][0]:4, lista[0][1]:1}  
        
    elif lista[1][2][0] == lista [1][2][1]:
        
        if lista[0][2][0] == lista[0][2][1]:
            return {lista[0][0]:2, lista[0][1]:2}
        
        elif lista[0][2][0] > lista[0][2][1]:
            return {lista[0][0]:4, lista[0][1]:1}
        
        elif lista[0][2][0] < lista[0][2][1]:
            return {lista[0][0]:1, lista[0][1]:4}