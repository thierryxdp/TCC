def melhor_volta(matriz):
    lista_tempo = []  
    lista_volta = [] 
    
    for corredores in range(6):  
        for voltas in range(10):  
            if matriz[corredores][voltas] == min(matriz[corredores]): 
                list.append(lista_tempo,voltas)  
    for i in range(6): 
        list.append(lista_volta,matriz[i][lista_tempo[i]])
    volta = lista_volta.index(min(lista_volta))
    tempo = min(lista_volta)
    corredor = matriz[volta].index(tempo) + 1
    
    tupla = (volta + 1, tempo, corredor)
    
    return tupla