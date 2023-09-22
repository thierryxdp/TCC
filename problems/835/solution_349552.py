def melhor_volta(m):
    '''
    list ----> tuple
    retorna tupla com o carro da melhor volta
    em que volta foi e quanto levou
    '''
   
    minimos=[]
    for i in range(len(m)):
        minimos+=[min(m[i]),m[i].index(min(m[i]))]
        
    minimo_final = [minimos[0][0]]
    for i in range(len(minimos)+1):
        for k in range(1):
            if minimo_final[0]<minimos[i+1][k]:
                minimo_final[0]=minimo_final[0]
                retorno = (i,minimo_final[0],minimos[i][1]) 
            else:
                minimo_final[0]=minimos[i+1][k]
                retorno = (i,minimo_final[0],minimos[i][1])
                
    return retorno