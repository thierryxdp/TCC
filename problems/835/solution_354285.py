def melhor_volta(matriz):
    '''Dada uma matriz 6x10, a função retorna uma tupla
    contendo o primeiro elemento da linha onde se encontra o 
    menor valor, o menor valor propriamente dito e o primeiro
    elemento da coluna onde o menor valor pode ser encontrado.
    list --> tuple''' 
    
    menores=()
    vencedor=0
    
    for corredor in matriz:
        for tempo in corredor:
            menores=menores+(min(corredor),)
            
    menor=min(menores)
    
    i=0
    while i<=5:
        if menores[i]==menor:
            vencedor=vencedor+i+1
        i=i+1
        
    return (vencedor,menor)