def pontos_por_time(a, b):
    '''Função que aponta a quantidade pontos de um time e sua classificação'''
    'dict(str,list),'
    a = a[0], a[1], a[2]
    b = b[0], b[1], b[2]
    
    resultados={'vitoria':3, 'derrota':0 , 'empate':1} 
    vitoria = 3
    derrota = 0
    empate =1
    dados={}
    pontos={}
               
      
    if a[2][0] > a[2][1] and b[2][1] > b[2][0]:
        return {a[0]:6, a[1]:0}
        
    if a[2][0] < a[2][1] and b[2][1] < b[2][0]:
        return
    if a[2][0] < a[2][1] and b[2][1] == b[2][0]:
        return
    if a[2][0] == a[2][1] and b[2][1] > a[2][0]:
        return
    if a[2][0] == a[2][1] and b[2][1] < b[2][0]:
        return
    if a[2][0] > a[2][1] and b[2][1] == b[2][0]:
    
        return
    else:
        return a