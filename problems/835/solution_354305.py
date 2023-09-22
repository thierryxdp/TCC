def melhor_volta(matriz):
    '''Dada uma matriz 6x10, a função retorna uma tupla
    contendo o primeiro elemento da linha onde se encontra o 
    menor valor, o menor valor propriamente dito e o primeiro
    elemento da coluna onde o menor valor pode ser encontrado.
    list --> tuple''' 
    
    menores=()
    
    
    for corredor in matriz:
        for tempo in corredor:
            menores=menores+(min(corredor),)
            
    menor=min(menores)
    

    i=0
    v=()
    
    for tempo in menores:   
        if tempo==menor:
            v=(list.index(tempo,menores)+1,)
       
        
    return (v,menor)