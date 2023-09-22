def media_matriz(matriz):
    """Dado uma matriz não vazia, retorna a média de todos os
    números da matriz, com precisão de duas casas decimais;
    list -> float"""
    total = [] 
    quantidade = 0
    for x in matriz :
        for y in x :
            list.append(total,y)
            quantidade = quantidade + 1 
            
    
    return round(sum(total)/quantidade, 2)