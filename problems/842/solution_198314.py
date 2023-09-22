def pontos_por_time(lista):
    jogo1_a = [0][2][0]
    jogo1_b = [0][2][1]
    jogo2_b = [1][2][0]
    jogo2_a = [1][2][1]
    
    if jogo1_a == jogo1_b:
        jogo1_a==1 and jogo1_b==1
       
    if jogo1_a > jogo1_b:
        jogo1_a=3 and jogo1_b=0
        
    if jogo1_a < jogo1_b:
        jogo1_a=0 and jogo1_b=3
        
    if jogo2_b == jogo2_a:
        [1][0]==1 and [1][1]==1
        
    if jogo2_b > jogo2_a:
        [1][0]==3 and [1][1]==0
        
    if jogo2_b < jogo2_a:
        [1][0]==0 and [1][1]==3
        
    ponto1 = [0][0] + [1][1]
    ponto2 = [0][1] + [1][0]
    
    return{[0][0]:ponto1, [0][1]:ponto2}