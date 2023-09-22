def pontos_por_time(a0, a1, a2,b0, b1, b2):
    '''Função que aponta a quantidade pontos de um time e sua classificação'''
    'dict(str,list)'
           
    resultados={'vitoria':3, 'derrota':0 , 'empate':1} 
    vitoria = 3
    derrota = 0
    empate =1
      
    Av=(a2[0]> a2[1],b2[0] < b2[1])
    Bv=(b2[0]> b2[1],a2[0] < a2[1])
    Ae=(a2[0]== a2[1],b2[0]== b2[1])
    
    if Av[0] and Av[1] == True :
        return (a0:6, a1:0)