def melhor_volta(matriz):
    '''Dada uma matriz 6x10, a função retorna uma tupla
    contendo o primeiro elemento da linha onde se encontra o 
    menor valor, o menor valor propriamente dito e o primeiro
    elemento da coluna onde o menor valor pode ser encontrado.
    list --> tuple''' 
    
    menores=()
    
    #para achar o menor tempo:
    for linha in matriz:
    	menores=menores+(min(linha),)
   
    menor_tempo=min(menores)
    
    i=0
    j=0
    volta=0
    
    while i<=5:
        if menor_tempo in matriz[i]:
            while j<=9:
            	if menor_tempo==matriz[i][j]:
                    volta=i+1
                j=j+1
        else:
            i=i+1
                
    
    #para achar o vencedor:
    i=0
    vencedor=0
    
    while i<=5:
        if menor_tempo==menores[i]:
            vencedor=i+1
        i=i+1
            
    return (vencedor,menor_tempo,volta)