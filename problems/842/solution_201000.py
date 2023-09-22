def pontos_por_time(x):
    '''Recebe uma lista de dois elementos, onde cada
    elemento tbm é uma lista. o parâmetro contém
    o seguinte formato: [['time1','time2',[pontuacao_time1, pontuacao_time2],
    ['time2', 'time1', [pontuacao_time2, pontuacao_time1]]]
    
    retorna um dicionario com o mapeamento:
    <nome do time> -> <numero total de pontos>
    
    list -> dict
    '''
    
	if x[0][2][0]>x[0][2][1] and x[1][2][1]>x[1][2][0]:
      
        return {x[0][0]:6,x[0][1]:0}
    
    elif x[0][2][0]==x[0][2][1] and x[1][2][1]==x[1][2][0]:
        
        return {x[0][0]:2,x[0][1]:2}
    
    
    elif x[0][2][0]<x[0][2][1] and x[1][2][1]<x[1][2][0]:
        
        return {x[0][0]:0,x[0][1]:6}
    
    elif x[0][2][0]>x[0][2][1] and x[1][2][0]>x[1][2][1]:
        
        return {x[0][0]:3,x[0][1]:3}
    
    elif x[0][2][0]<x[0][2][1] and x[1][2][1]>x[1][2][0]:
        
        return {x[0][0]:3,x[0][1]:3}
    
    elif x[0][2][0]<x[0][2][1] and x[1][2][1]==x[1][2][0]:
        
        return {x[0][0]:1,x[0][1]:4}
    
    else:
        
        return {x[0][0]:1,x[0][1]:4}