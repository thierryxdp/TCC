def pontos_por_time(l1, l2):
    pontos = [0, 0] # cormengo, flaminthians
    
    # jogo de ida
    if(l1[0] == "Cormengo"):
       if(l1[2][0] > l1[2][1]): # vitoria
       		pontos[0] = 3
       elif(l1[2][0] == l1[2][1]): # empate
        	pontos[0] = 1
    
    if(l1[0] == "Flamínthians"):
       if(l1[2][0] > l1[2][1]): # vitoria
       		pontos[1] = 3
       elif(l1[2][0] == l1[2][1]): # empate
        	pontos[1] = 1
    
    
    
    # jogo de volta
    if(l2[0] == "Cormengo"):
       if(l2[2][0] > l2[2][1]): # vitoria
       		pontos[0] = pontos[0] + 3
       elif(l2[2][0] == l2[2][1]): # empate
        	pontos[0] = pontos[0] + 1
    
    if(l2[0] == "Flamínthians"):
       if(l2[2][0] > l2[2][1]): # vitoria
       		pontos[1] = pontos[1] + 3
       elif(l2[2][0] == l2[2][1]): # empate
        	pontos[1] = pontos[1] + 1
    
    return {"Cormengo" : pontos[0], "Flamínthians": pontos[1]}