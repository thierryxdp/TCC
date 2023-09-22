def pontos_por_time(x):#Start your python function here
    '''Função que retorna um dicionário com o nome dos times e a pontuação na fase'''
    
    if x[0][2][0]>x[0][2][1] and x[1][2][1]>x[1][2][0]:
      
        return {x[0][0]:6,x[0][1]:0}
    
    elif x[0][2][0]==x[0][2][1] and x[1][2][1]==x[1][2][0]:
        
        return {x[0][0]:2,x[0][1]:2}