def pontos_por_time(x):
    '''função que que dado resultado de jogos, retorna o
    total de ponto de um dado time
    ass: lista[lista]--> dicionario
    '''
    
    dic={x[0][0]:0,x[0][1]:0}
    if x[0][2][0] > x[0][2][1]:
         dic[x[0][0]] = dic[x[0][0]]+3
            
    if x[0][2][0] < x[0][2][1]:
         dic[x[0][1]]= dic [x[0][1]]+3
            
    if x[0][2][0] == x[0][2][1]:
        dic [x[0][0]]= dic [x[0][0]]+1
        dic [x[0][1]]= dic [x[0][1]]+1
        
    if x[1][2][0] < x[1][2][1]:
         dic[x[0][0]] = dic[x[0][0]]+3
            
    if x[1][2][0] > x[1][2][1]:
         dic[x[0][1]]= dic[x[0][1]]+3
            
    if x[1][2][0] == x[1][2][1]:
        dic[x[0][0]]= dic[x[0][0]]+1
        dic[x[0][1]]= dic[x[0][1]]+1
    return dic