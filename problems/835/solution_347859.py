def melhor_volta(matriz):
    '''retorna uma tupla com a linha e coluna da melhor volta 
    inserida na lista do 1 arg
    list(list) -> tuple'''
    
    menor = 0
    min = 0
    
    for i in range(len(matriz)):
        
        menos = min(matriz[i])
        
        if i == 0:
            menor = matriz[i]
            
        if i != 0 and menor >= min(matriz[i-1]):
            menor = min(matriz[i-1])
          
        coluna = list.index(menor,matriz[i])  
    
    return (i+1,menor,coluna+1)