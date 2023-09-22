def pontos_por_time(Lista):
    """calcula e retorna o estado de um time em um campeonato:List->dic"""
 
    if Lista[0][2][0]==Lista[0][2][1]:
        if Lista[1][2][0]==Lista[1][2][1]:
            p={Lista[0][0]:2,Lista[0][1]:2} 
        elif Lista[1][2][0]>Lista[1][2][1]:
            p={Lista[0][0]:4,Lista[0][1]:1}
        elif Lista[1][2][0]<Lista[1][2][1]:
            p={Lista[0][0]:4,Lista[0][1]:1}
    elif Lista[0][2][0]>Lista[0][2][1]:        
        if Lista[1][2][0]==Lista[1][2][1]:
            p={Lista[0][0]:4,Lista[0][1]:1}
        elif Lista[1][2][0]>Lista[1][2][1]:
            p={Lista[0][1]:0,Lista[0][0]:6}
        elif Lista[1][2][0]<Lista[1][2][1]:
            p={Lista[0][0]:3,Lista[0][1]:3} 
    elif Lista[0][2][0]<Lista[0][2][1]:
        if Lista[1][2][0]==Lista[1][2][1]:
            p={Lista[0][0]:1,Lista[0][1]:4}
        elif Lista[1][2][0]>Lista[1][2][1]:
            p={Lista[0][1]:6,Lista[0][0]:0}
        elif Lista[1][2][0]<Lista[1][2][1]:
            p={Lista[0][0]:3,Lista[0][1]:3}
    else:
        p={Lista[0][0]:0,Lista[0][1]:0}
        
        return p