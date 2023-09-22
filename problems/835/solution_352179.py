def melhor_volta(matriz):
    l=0
    m=0
    tempo= 999999999999999999999999999999999999
    piloto=0
    volta=0
    while l < len(matriz):
        #len(matriz)= corredores
        while m < len(matriz[0]):
            #tempos= len(matriz[0])
            tempo1= matriz[l][m]
            if tempo1 < tempo :
                tempo= tempo1
                piloto = l +1
                volta= m + 1
            
            m+=1    
                
        l+=1
    return piloto,tempo,volta