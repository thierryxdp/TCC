def pontos_por_time(lista):
    """."""
    cor = lista[0][2]
    fla = lista[1][3]
    
    if lista[0]+[2] > lista[1][3]:
        pontoscor = 3
        pontosfla = 0
        
    if lista[0]+[2] < lista[1][3]:
        pontoscor = 0
        pontosfla = 3
        
        return {cor:pontoscor, fla:pontosfla}