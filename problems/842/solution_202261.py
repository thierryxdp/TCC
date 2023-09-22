def pontos_por_time(lista):
    """."""
    time1 = lista[0][0]
    time2 = lista[0][1]
    
    if lista[0][2][0] > lista[0][2][1]:
        pontostime1j1 = 3
        pontostime2j1 = 0
        
    if lista[0][2][0] < lista[0][2][1]:
        pontostime1j1 = 0
        pontostime2j1 = 3
       
    if lista[0][2][0] == lista[0][2][1]:
        pontostime1j1 = 1
        pontostime2j1 = 1
        
        
    if lista[1][2][0] > lista[1][2][1]:
        pontostime1j2 = 3
        pontostime2j2 = 0
        
    if lista[1][2][0] < lista[1][2][1]:
        pontostime1j2 = 0
        pontostime2j2 = 3
       
    if lista[1][2][0] == lista[1][2][1]:
        pontostime1j2 = 1
        pontostime2j2 = 1
        
        pt1 = pontostime1j1 + pontostime1j2
        pt2 = pontostime2j1 + pontostime2j2
        
        
        return {time1:pt1, time2:pt2}