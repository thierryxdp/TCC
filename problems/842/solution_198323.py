def pontos_por_time(lista):
    jogo1_a = lista[0][2][0]
    jogo1_b = lista[0][2][1]
    jogo2_b = lista[1][2][0]
    jogo2_a = lista[1][2][1]
    
    ponto1 = jogo1_a + jogo2_a
    ponto2 = jogo1_b + jogo2_b
    
    if jogo1_a == jogo1_b:
        jogo1_a = 1 
        jogo1_b = 1
        
    if jogo1_a > jogo1_b:
        jogo1_a==3 and jogo1_b==0 
    
    if jogo1_a < jogo1_b:
        jogo1_a==0 and jogo1_b==3
        
    if jogo2_b == jogo2_a:
        jogo2_b==1 and jogo2_a==1
        
    if jogo2_b > jogo2_a:
        jogo2_b==3 and jogo2_a==0
        
    if jogo2_b < jogo2_a:
        jogo2_b==0 and jogo2_a==3
    
    return jogo1_a