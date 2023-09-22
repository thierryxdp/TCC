lista[[time],[placar]],[time,[placar]]]

[[cormengo,flamintians,[1,0]],[flamintians,cormengo,[2,2]]]
vitoria- 3 pontos
empate - 1 ponto


dicio = [nome time, numero pontos]

lista3 = []
    
    if lista1[0][2][0] > lista1[0][2][1]:
        lista3 = lista3 + [lista1[0][0],3]
        
    elif lista1[0][2][0] < lista1[0][2][1]:
        lista3 = lista3 + [lista1[0][1],3]
        
    elif lista1[0][2][0] == lista1[0][2][1]:
       lista3 = lista3 + [lista1[0][0],1,lista1[0][1],1]

       lista4 = []

    elif lista1[1][2][0] > lista1[1][2][1]:
        lista4 = lista4 + [lista1[1][0],3] 
        
    elif lista1[1][2][0] < lista1[1][2][1]:
        lista4 = lista4 + [lista1[1][1]:3]
        
    elif lista1[1][2][0] == lista1[1][2][1]:
      lista4 = lista4 + [lista1[1][0]:1,lista1[1][1]:1]


      lista3 - 1 jogo (time,saldo)
      lista4 - 2 jogo (time,saldo)

      return {lista3, lista4}